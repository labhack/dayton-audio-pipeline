import os
import glob
import requests
from requests.auth import HTTPBasicAuth
import json

url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize'
name = os.getenv('watson_name')
password = os.getenv('watson_password')

file_paths = glob.glob('*.WAV')

for i in range(0, len(file_paths)):
   FilePath = file_paths[i]

   FileData = open(FilePath, 'rb')

   length = os.path.getsize(FilePath)

   headers = {'Content-Type': 'audio/wav', 'Content-Length': length}

   r = requests.post(url=url, headers=headers, auth=HTTPBasicAuth(name, password), data=FileData)

   with open(os.path.splitext(FilePath)[0] + '.json', 'w') as outfile:
    json.dump(r.json(), outfile)
