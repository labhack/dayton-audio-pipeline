#!/usr/bin/env python
#
# first input argument is name of inputFile to parse and segment

# I created a fork of this repo:
# https://github.com/tyiannak/pyAudioAnalysis @ 3799c3ab4cc5d0d5f8d60e9105f0d59f74976909
# at
# https://github.com/anielsen001/pyAudioAnalys to put labhack mods
# find ~/sw/pyAudioAnalysis/audioAnalysis.py

# this example worked:
# from: https://github.com/tyiannak/pyAudioAnalysis/wiki/5.-Segmentation
# python audioAnalysis.py speakerDiarization -i '/home/apn/labhack/data/Initial Audio Files/Dayton Fire Department/1141 Main/Recorded on 30-Oct-2007 at 09.49.53 ()YWJFT8D02357272)-clean.wav' --num 0

REDO = False

# add logging information
import logging
mylog = logging.getLogger('segmentation')
mylog.level = logging.DEBUG
ch = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(name)s - %(message)s')
ch.setFormatter(formatter)
mylog.addHandler(ch)

import sys,os
sys.path.append('/home/apn/sw/pyAudioAnalysis') # for pyAudioAnalysis

import numpy as np

# audioSegmentation is in pyAudioAnalysis
import audioSegmentation as aS

# this stub called the speaker diarization in the original
#def speakerDiarizationWrapper(inputFile, numSpeakers, useLDA):
#    if useLDA:
#        aS.speakerDiarization(inputFile, numSpeakers, PLOT=True)
#    else:
#        aS.speakerDiarization(inputFile, numSpeakers, LDAdim=0, PLOT=True)

# speaker diarization function from audioSegmentation.py
#def speakerDiarization(fileName, numOfSpeakers, mtSize=2.0, mtStep=0.2, stWin=0.05, LDAdim=35, PLOT=False):
#    '''
#    ARGUMENTS:
#        - fileName:        the name of the WAV file to be analyzed
#        - numOfSpeakers    the number of speakers (clusters) in the recording (<=0 for unknown)
#        - mtSize (opt)     mid-term window size
#        - mtStep (opt)     mid-term window step
#        - stWin  (opt)     short-term window size
#        - LDAdim (opt)     LDA dimension (0 for no LDA)
#        - PLOT     (opt)   0 for not plotting the results 1 for plottingy
#    '''
#
#### this function does not return anything by default, it just makes plots
#### I will add return of segmentation data to it.

# Need to use the sox command to get this to work:
# sox "raw/Recorded on 19-Feb-2009 at 19.26.28 (-AIOR50)02357272).WAV" -b16 clean/clean.wav

# there are hard-coded paths in audioSegmentation.py to a data directory
# i.e. data/knnSpeakerAll and data/knnSpeakerFemaleMale
# these need to be overridden, for now, I hard-coded audioSegmentation.py to my full path
# used a variable DATA_DIR at the top of audioSegmentation.py

# find the input file - first input argument - allow arbitrary input files
inputFiles = sys.argv[1:]
# hardcode for test
#inputFile = '/home/apn/labhack/data/Initial Audio Files/Dayton Fire Department/1141 Main/Recorded on 30-Oct-2007 at 09.49.53 ()YWJFT8D02357272)-clean.wav'

def dumbWriteFunc(f,segmentId,speakerId,startTime,stopTime):
    txt = '%d, %d, %f, %f'%(\
                                segmentId,
                                speakerId,
                                startTime,
                                stopTime)
    f.write(txt + '\n')
    return None
        

for inputFile in inputFiles:

    mylog.info('Segmenting: %s',inputFile)
    
    # not sure how this code handles multiple channels in the inputFile

    numOfSpeakers = 0 # set to zero for unknown - algorithm decides
                      # set to number if known

    # use the indices to write out a text file containing the timing information
    # for segmentation
    dirname,basename = os.path.split(inputFile)
    basename,ext     = os.path.splitext(basename)
    outFile          = os.path.sep.join([dirname,basename + '-seg.txt']) 
                      
    try:
        segInfo = aS.speakerDiarization(inputFile,numOfSpeakers)
    except:
        # if the segmentation fails, log it and continue
        # the code will fail if there is only one speaker in the file
        # i.e. this file ./Initial Audio Files/Dayton Fire Department/Haz-Mat Incident/14-23-28-clean.wav
        mylog.warning('Segmentation failed: %s', inputFile)

        with open(outFile,'w') as f:
            # write a single line to the file, -1 as duration indicates entire file
            dumbWriteFunc(f,0,0,0.0,-1.0)
        continue

    # segInfo contains a list
    # segInfo[0] is the time step of the analysis
    # segInfo[1] is np array of the speaker ID at each time step

    # find the difference
    dId = np.diff(segInfo[1])

    # anywhere that dId is non-zero the speaker changes
    chgId = np.where(dId!=0)[0]

    # if outFile exists and we set REDO, then process, otherwise skip
    if os.path.isfile(outFile) and not REDO:
        mylog.info('%s exists, skipping',outFile)
        continue
        

    with open(outFile,'w') as f:

        for ii,idx in enumerate(chgId):
            # write a line for each segment
            segmentId = ii
            speakerId = segInfo[1][chgId[ii]]
            startTime = chgId[ii-1]*segInfo[0] if ii>0 else 0.0
            stopTime  = chgId[ii]*segInfo[0]
            dumbWriteFunc(f,segmentId,speakerId,startTime,stopTime)
        # there is one final segment to account for
        segmentId += 1
        speakerId  = segInfo[1][-1]
        startTime  = stopTime
        stopTime   = len(segInfo[1])*segInfo[0]
        dumbWriteFunc(f,segmentId,speakerId,startTime,stopTime)

        
# for interferer mitigtation consider:
# Non-Stationary Gabor Transform http://grrrr.org/research/software/nsgt/
# python code here: https://github.com/grrrr/nsgt
# reference here: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4111459/
#
# python adaptive filters:
# https://github.com/matousc89/padasip
