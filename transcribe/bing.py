"""
run this with ipython - not with python!
preprocess the .wav from ADPCM to PCM by using:
`sox <old_filepath> -b16 <new_filepath>
"""

import speech_recognition as sr
import os
import sys

class Transcriber(object):
    name = 'bing'

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.API_KEY = os.getenv('BING_KEY')
        if not self.API_KEY:
            raise Exception('Environment variable BING_KEY required')

    def json(self, filepath):
        with sr.AudioFile(filepath) as source:
            audio = self.recognizer.record(source)
        text = self.recognizer.recognize_bing(audio, key=self.API_KEY)
        return {'transcriber': self.name, 'text': text}
