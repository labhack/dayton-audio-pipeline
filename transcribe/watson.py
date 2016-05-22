import os
import glob
import requests
from requests.auth import HTTPBasicAuth
import json


class Transcriber(object):
    name = 'watson'
    url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=en-US_NarrowbandModel'

    # url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=en-US_NarrowbandModel&word_confidence=true&timestamps=true&max_alternatives=3&word_alternatives_threshold=0.3&continuous=false&inactivity_timeout=30&keywords_threshold=0.1'

    def __init__(self):
        self.name = os.getenv('watson_name')
        if not self.name:
            raise Exception('Environment variable watson_name required')

        self.password = os.getenv('watson_password')
        if not self.password:
            raise Exception('Environment variable watson_password required')

    def json(self, filepath):
        FileData = open(filepath, 'rb')
        length = os.path.getsize(filepath)
        headers = {'Content-Type': 'audio/wav', 'Content-Length': length}
        resp = requests.post(url=self.url, headers=headers, auth=HTTPBasicAuth(self.name, self.password), data=FileData)
        return resp.json()
