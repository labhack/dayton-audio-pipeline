import os
import glob
import requests
from requests.auth import HTTPBasicAuth
import json

url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize'
name = '91acc080-c273-4054-b16b-a11e70e3a591'
password = 'aqkRteMdUXmF'

file_paths = glob.glob('*.WAV')

for i in range(0, len(file_paths)):
   FilePath = file_paths[i]

   FileData = open(FilePath, 'rb')

   length = os.path.getsize(FilePath)

   headers = {'Content-Type': 'audio/wav', 'Content-Length': length}

   r = requests.post(url=url, headers=headers, auth=HTTPBasicAuth(name, password), data=FileData)

   with open(os.path.splitext(FilePath)[0] + '.json', 'w') as outfile:
    json.dump(r.json(), outfile)