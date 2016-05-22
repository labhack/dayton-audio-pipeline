"""
run this with ipython - not with python!
preprocess the .wav from ADPCM to PCM by using:
`sox <old_filepath> -b16 <new_filepath>
"""

import logging
import click
import glob
import json
import os
import subprocess
import time
import re

import bing, watson

SOX_CLEANSED_FILENAME = '_cleansed_with_sox.wav'

# logging.basicConfig(level=logging.DEBUG)

elapsed_parser = re.compile(r'(?P<hr>\d\d):(?P<min>\d\d):(?P<sec>\d\d)\.(?P<hsec>\d\d)\s')
def audio_file_stats():
    raw_result = subprocess.check_output(['soxi', SOX_CLEANSED_FILENAME])
    raw_result = raw_result.decode('utf8')
    result = {}
    for line in raw_result.strip().splitlines():
        (k, v) = line.split(':', 1)
        result[k.strip()] = v.strip()
        if k.strip() == 'Duration':
            elapsed = elapsed_parser.search(v).groupdict()
            result['seconds'] = int(elapsed['hr']) * 3600 + int(elapsed['min']) * 60 + int(elapsed['sec']) + int(elapsed['hsec']) * 0.01
    return result

@click.command()
@click.argument('filepaths', nargs=-1, required=True)
@click.option('-e', '--engine', default='watson',
              help='Speech-to-text engine: watson or bing')
@click.option('-p', '--play', type=bool, default=False,
    help='Use `open` (on mac) to play the audio')
def transcribe(engine, play, filepaths):
    logging.debug('Begin transcribing engine {} filepath {}'.
        format(engine, filepath))
    if engine == 'bing':
        transcriber = bing.Transcriber()
    else:
        transcriber = watson.Transcriber()
    for filepattern in filepaths:
        for filepath in glob.glob(filepattern):
            logging.info('Playing the file')
            logging.info('Applying {} to {}'.format(transcriber.name, filepath))
            logging.info('{} bytes'.format(os.stat(filepath).st_size))
            logging.info('applying sox')
            logging.info('timing...')
            result = json.dumps(transcriber.json(filepath), indent=2)
            yield result

@click.command()
@click.option('-e', '--engine', default='watson',
              help='Speech-to-text engine: watson or bing')
@click.option('-p', '--play', type=bool, default=False,
    help='Use `open` (on mac) to play the audio')
@click.argument('filepaths', nargs=-1, required=True)
def transcribe(engine, play, filepaths):
    logging.debug('Begin transcribing engine {} filepath {}'.
        format(engine, filepaths))
    if engine == 'bing':
        transcriber = bing.Transcriber()
    else:
        transcriber = watson.Transcriber()
    result = {}
    for filepattern in filepaths:
        for filepath in glob.glob(filepattern):
            logging.info('Applying {} to {}'.format(transcriber.name, filepath))
            logging.debug('applying sox')
            subprocess.call(['sox', filepath, '-b16', SOX_CLEANSED_FILENAME])
            start_time = time.monotonic()
            result[filepath] = transcriber.json(SOX_CLEANSED_FILENAME)
            result[filepath]['file_stats'] = audio_file_stats()
            result[filepath]['size_bytes'] = os.stat(SOX_CLEANSED_FILENAME).st_size
            result[filepath]['elapsed_seconds'] = time.monotonic() - start_time
    print(json.dumps(result, indent=2))
    return result

if __name__ == '__main__':
    transcribe()
