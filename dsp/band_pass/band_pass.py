#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Band Pass
# Generated: Sun May 22 10:18:22 2016
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class band_pass(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Band Pass")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 16000
        self.low_cutoff = low_cutoff = 1000
        self.high_cutoff = high_cutoff = 2000
        self.transition_width = transition_width = 10
        self.input_file = ""
        self.output_file = ""
        
        self.update_filter()
        
        ##################################################
        # Blocks
        ##################################################
        
        

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 1000, 4000, 10, firdes.WIN_HAMMING, 6.76))

    def update_filter(self):
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, self.samp_rate, self.low_cutoff, self.high_cutoff, self.transition_width, firdes.WIN_HAMMING, 6.76))
        	
    def setup_blocks(self):
        self.connect((self.band_pass_filter_0, 0), (self.blocks_wavfile_sink_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0, 0)) 
        
    def update_wav_source(self):
        self.blocks_wavfile_source_0 = blocks.wavfile_source(self.input_file, False)
        
    def update_wav_sink(self):
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(self.output_file, 1, self.samp_rate, 16)
        
    def set_low_cutoff(self, cutoff):
        self.low_cutoff = cutoff
        self.update_filter()
        
    def set_high_cutoff(self, cutoff):
        self.high_cutoff = cutoff
        self.update_filter()
        
    def set_transition_width(self, transition_width):
        self.transition_width = transition_width
        self.update_filter()
        
    def set_input_file(self, input_file):
        self.input_file = str(input_file)
        self.update_wav_source()
        
    def set_output_file(self, output_file):
        self.output_file = str(output_file)
        self.update_wav_sink()
