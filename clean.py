#!/usr/bin/env python2.7
#
# run the sox command to clean all the files
#
# I used like this:
# find . -iname "*wav" -print0 | xargs -0 ../sw/dayton-audio-pipeline/clean.py 
# to clean all the files

import sys,os

import logging
log = logging.getLogger('clean')
log.level = logging.DEBUG
ch = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(name)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

if __name__=='__main__':
    # input is arbitrary list of input files
    infiles = sys.argv[1:]

    # output will be infile name with -clean inserted ahead of .wav

    for infile in infiles:
        dirname,basename = os.path.split(infile)
        basename,ext     = os.path.splitext(basename)
        outfile          = os.path.sep.join([dirname,basename + '-clean.wav'])

        # create the sox command
        cmd = 'sox ' + repr(infile) + ' -b16 ' + repr(outfile)
        log.info(cmd)   # log the command
        os.system(cmd)  # run the command

        
    
    
