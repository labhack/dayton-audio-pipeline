import os
import glob
import requests
from requests.auth import HTTPBasicAuth
import json
import urllib

keywords = 'one,read'

url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=en-US_BroadbandModel&word_confidence=true&timestamps=true&max_alternatives=3&word_alternatives_threshold=0.3&continuous=false&inactivity_timeout=30&keywords_threshold=0.1'

keywordsParam = urllib.quote_plus(keywords)
keywordsParam = keywordsParam.replace("+", "%20")
url = url + '&keywords=' + keywordsParam

name = ''
password = ''

file_paths = glob.glob('*.WAV')

for i in range(0, len(file_paths)):
   FilePath = file_paths[i]

   FileData = open(FilePath, 'rb')

   length = os.path.getsize(FilePath)

   headers = {'Content-Type': 'audio/wav'}

   r = requests.post(url=url, headers=headers, auth=HTTPBasicAuth(name, password), data=FileData)

   jsonOutput = json.loads(r.text)

   #print jsonOutput

   jsonFile = open(os.path.splitext(FilePath)[0] + '.json','w')
   jsonFile.write(json.dumps(jsonOutput))
   jsonFile.close()

   transcriptText = jsonOutput['results'][0]['alternatives'][0]['transcript']

   transcriptFile = open(os.path.splitext(FilePath)[0] + '.txt','w')
   transcriptFile.write(transcriptText)
   transcriptFile.close()
