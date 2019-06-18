import requests
import json
import pandas as pd

vocab = pd.read_csv('words.csv')

app_id = '<app_id>'
app_key = '<app_key>'

language = 'en-us'
fields = ''
strictMatch = 'false'
url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/'

for row in vocab.index:
	word = vocab['Word'][row]
	r = requests.get(url + word, headers = {'Accept': 'application/json', 'app_id': app_id, 'app_key': app_key})
	if r.status_code == 200:
		json_obj = r.json()
		if 'definitions' in json_obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]:
			vocab['Meaning'][row] = json_obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
		if 'examples' in json_obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]:
			vocab['Sentence'] = json_obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text']

vocab.to_csv('words.csv')
