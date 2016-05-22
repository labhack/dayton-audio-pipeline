import os
import glob
import requests
from requests.auth import HTTPBasicAuth
import json


class Transcriber(object):
    name = 'watson'

    url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=en-US_NarrowbandModel&word_confidence=true&timestamps=true&max_alternatives=3&word_alternatives_threshold=0.3&continuous=false&inactivity_timeout=30&keywords_threshold=0.1'
    toneURL = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2016-05-18'
            

    def __init__(self):
        self.name = os.getenv('watson_name')
        if not self.name:
            raise Exception('Environment variable watson_name required')

        self.password = os.getenv('watson_password')
        if not self.password:
            raise Exception('Environment variable watson_password required')

        self.tone_name = os.getenv('watson_tone_name')
        if not self.tone_name:
            raise Exception('Environment variable watson_tone_name required')

        self.tone_password = os.getenv('watson_tone_password')
        if not self.tone_password:
            raise Exception('Environment variable watson_tone_password required')

        self.keywords = os.getenv('watson_keywords')
        if not self.keywords:
            raise Exception('Environment variable watson_keywords required')

    def json(self, filepath):

        keywordsParam = urllib.quote_plus(keywords)
        keywordsParam = keywordsParam.replace("+", "%20")
        url = url + '&keywords=' + keywordsParam

        FileData = open(filepath, 'rb')
        length = os.path.getsize(filepath)
        headers = {'Content-Type': 'audio/wav', 'Content-Length': length}
        resp = requests.post(url=self.url, headers=headers, auth=HTTPBasicAuth(self.name, self.password), data=FileData)

        jsonOutput = json.loads(r.text)

        if len(jsonOutput['results']) > 0:

            transcriptText = jsonOutput['results'][0]['alternatives'][0]['transcript']

            transcriptFile = open(os.path.splitext(filepath)[0] + '.txt','w')
            transcriptFile.write(transcriptText)
            transcriptFile.close()

            testText = '{\"text\": \" + transcriptText + \"}'

            toneHeader = {'Content-Type': 'application/json'}

            toneRequest = requests.post(url=toneURL, headers=toneHeader, auth=HTTPBasicAuth(toneName, tonePassword), data=testText)

            toneFile = open(os.path.splitext(filepath)[0] + 'Tone.txt','w')
            toneFile.write(toneRequest.text)
            toneFile.close()

        return resp.json()
