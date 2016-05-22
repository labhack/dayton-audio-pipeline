#!/usr/bin/env python2.7
#
# create a spectrogram of input wav file for analysis
#
# I used like this:
# find . -iname "*wav" -print0 | xargs -0 ../sw/dayton-audio-pipeline/make_specgram.py 
# to clean all the files

import sys,os

import logging
mylog = logging.getLogger('specgram')
mylog.level = logging.DEBUG
ch = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(name)s - %(message)s')
ch.setFormatter(formatter)
mylog.addHandler(ch)

import numpy as np              # everyone needs numpy

import matplotlib
#matplotlib.use('Agg')
from matplotlib.pylab import *  # includes plotting and specgram routines
ioff()                          # interactive off for matplotlib

from scipy.io import wavfile    # wavefile read and write routines

db10 = lambda x: 10.0 * np.log10(np.abs(x))
db20 = lambda x: 20.0 * np.log10(np.abs(x))

# a list of bad characters to removes from filenames for display in matplotlib
badchars = '()^${}#?/'

if __name__=='__main__':
    # input is arbitrary list of input files
    infiles = sys.argv[1:]

    # output will be infile name with -clean inserted ahead of .wav

    for infile in infiles:
        # manipulate file names
        dirname,basename = os.path.split(infile)
        basename,ext     = os.path.splitext(basename)
        outfile_info     = os.path.sep.join([dirname,basename + '-info.txt'])

        # log the working file
        mylog.info('Processing: %s',infile)   

        # read the file
        wav = wavfile.read(infile)
        # wav = (Fs,data)
        # Fs  = sampling rate in Hz
        # data is raw data read from file

        # the wave file may contain multiple channels, e.g. stereo?
        try:
            nchans   = wav[1].shape[1]
        except IndexError:
            nchans   = 1

        totTime  = len(wav[1])/float(wav[0])
        bitDepth = str(wav[1].dtype)
                                    
        # output a text file with some basic information
        with open(outfile_info,'w') as f:
            txt = ', '.join([basename,
                             str(wav[0]),
                             str(totTime),
                             str(bitDepth),
                             str(nchans)])
            f.write(txt + '\n')

        if totTime > 300.0:
            # don't process files longer than 300 seconds - 5 minutes
            mylog.warning('%s is %f long, skipping',basename,totTime)
            continue
            
        # create time series and specgram for each channel in wave file
        for ichan in range(nchans):
            outfile_sg       = os.path.sep.join([dirname,basename + '-specgram-' + str(ichan) +'.png'])
            outfile_ts       = os.path.sep.join([dirname,basename + '-timeseries-' + str(ichan) +'.png'])

            # fix a bad basename for display on plots
            basename_plot = basename.translate(None,badchars)
            
            try:
                chandata = wav[1][:,ichan]
            except IndexError:
                chandata = wav[1]

            # matplotlib command to create the time series
            timeAxis = np.arange(len(chandata))/float(wav[0])
            fig = figure()
            plot(timeAxis,chandata)
            grid()
            xlabel('Time [sec]')
            ylabel('Amplitude [AU]')
            title(basename_plot)
            savefig(outfile_ts)
            close(fig)

            # create the spectorgram
            sg = specgram(chandata,
                          NFFT=2**10,
                          Fs=wav[0],
                          window=window_hanning,
                          noverlap=2**9,
                          detrend=detrend_mean)


            # this the matplotlib command to create the figure
            figure()
            imshow(db10(sg[0]),aspect='auto',extent=[sg[2][0],sg[2][-1],sg[1][-1],sg[1][0]])
            xlabel('Time [sec]')
            ylabel('Frequency [Hz]')
            title(basename_plot)
            savefig(outfile_sg)
            colorbar()
            close(fig)


    
    
