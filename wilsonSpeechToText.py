import os
import glob
import requests
from requests.auth import HTTPBasicAuth
import json
import urllib

keywords = 'one,read'

url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=en-US_NarrowbandModel&word_confidence=true&timestamps=true&max_alternatives=3&word_alternatives_threshold=0.3&continuous=false&inactivity_timeout=30&keywords_threshold=0.1'

keywordsParam = urllib.quote_plus(keywords)
keywordsParam = keywordsParam.replace("+", "%20")
url = url + '&keywords=' + keywordsParam

name = '286a8577-9c0b-4a6c-946e-93ac49cf71b8'
password = 'J44aZuUWhf4g'

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

   if len(jsonOutput['results']) > 0:

       transcriptText = jsonOutput['results'][0]['alternatives'][0]['transcript']

       transcriptFile = open(os.path.splitext(FilePath)[0] + '.txt','w')
       transcriptFile.write(transcriptText)
       transcriptFile.close()

       testText = '{\"text\": \" + transcriptText + \"}'

       toneURL = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2016-05-18'
       toneName = 'cb5d40f5-ae33-4805-93b9-47760486f96f'
       tonePassword = 'wrJWJJkU1nGu'
       toneHeader = {'Content-Type': 'application/json'}

       toneRequest = requests.post(url=toneURL, headers=toneHeader, auth=HTTPBasicAuth(toneName, tonePassword), data=testText)

       toneFile = open(os.path.splitext(FilePath)[0] + 'Tone.txt','w')
       toneFile.write(toneRequest.text)
       toneFile.close()

   
