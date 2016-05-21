"""
run this with ipython - not with python!
preprocess the .wav from ADPCM to PCM by using:
`sox <old_filepath> -b16 <new_filepath>
"""

import speech_recognition as sr
import os
import sys

BING_KEY = os.getenv('BING_KEY')

def text(filepath):
    r = sr.Recognizer()
    with sr.AudioFile(filepath) as source:
        audio = r.record(source) # read the entire audio file
    return r.recognize_bing(audio, key=BING_KEY)
    # return r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
    # return r.recognize_sphinx(audio)

if __name__ == '__main__':
    filepath = sys.argv[1]
    get_ipython().system('open "{}"'.format(filepath))
    print('{} bytes'.format(os.stat(filepath).st_size))
    print('Transcript:')
    print(text(filepath))
