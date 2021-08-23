'''
curl -X POST --user "apikey:k7QWwjJo5sbaM0Ld_X7DIxg89BX1FjZ1zEYSUbgChKAg"  --header "Content-Type: application/json"  --data '{"text": ["Hello, world.", "How are you?"], "model_id":"en-fr"}'  "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/d6419df8-d196-4118-b61f-092cabd9a680/v3/translate?version=2018-05-01"
'''

import requests
from requests.auth import HTTPBasicAuth #ibm watson api used basic authentication
import json

KEY="k7QWwjJo5sbaM0Ld_X7DIxg89BX1FjZ1zEYSUbgChKAg"
URL="https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/d6419df8-d196-4118-b61f-092cabd9a680/v3/translate"
hdrs = {'Content-Type': 'application/json'}

class Translator(object):
    def __init__(self):
        None
    def EnglishToFrench(self, english_sentence):
        values = {'text': [english_sentence],
                  'model_id': 'en-fr'}
        version={'version': '2018-05-01'}
        res=requests.post(url=URL, data=json.dumps(values), auth=HTTPBasicAuth('apikey', KEY), params=version, headers=hdrs)
        response=res.json()
        translations = response["translations"][0]
        return translations['translation']

    def FrenchToEnglish(self, french_sentence):
        values = {'text': [french_sentence],
                  'model_id': 'fr-en'}
        version={'version': '2018-05-01'}
        res=requests.post(url=URL, data=json.dumps(values), auth=HTTPBasicAuth('apikey', KEY), params=version, headers=hdrs)
        response=res.json()
        translations = response["translations"][0]
        return translations['translation']

translator = Translator()
