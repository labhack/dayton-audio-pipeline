"""
run this with ipython - not with python!
preprocess the .wav from ADPCM to PCM by using:
`sox <old_filepath> -b16 <new_filepath>
"""

import speech_recognition as sr
import os
import sys

BING_KEY='5755fcdf9fd340818436512ccbc82fda'

def text(filepath):
    r = sr.Recognizer()
    with sr.AudioFile(filepath) as source:
        audio = r.record(source) # read the entire audio file
    return r.recognize_bing(audio, key=BING_KEY)

if __name__ == '__main__':
    filepath = sys.argv[1]
    get_ipython().system('open "{}"'.format(filepath))
    print('{} bytes'.format(os.stat(filepath).st_size))
    print('Transcript:')
    print(text(filepath))
