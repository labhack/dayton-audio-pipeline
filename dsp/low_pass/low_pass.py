#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Low Pass
# Generated: Sun May 22 10:19:45 2016
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class low_pass(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Low Pass")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 16000
        self.cutoff = cutoff = 1000
        self.transition_window = transition_window = 10
        self.input_file = ""
        self.output_file = ""
        
        self.update_filter()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.transition_window, firdes.WIN_HAMMING, 6.76))

    def update_filter(self):
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, self.samp_rate, self.cutoff, self.transition_window, firdes.WIN_HAMMING, 6.76))

    def setup_blocks(self):
        self.connect((self.blocks_wavfile_source_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_wavfile_sink_0, 0))  
        
    def update_wav_source(self):
        self.blocks_wavfile_source_0 = blocks.wavfile_source(self.input_file, False)
    
    def update_wav_sink(self):
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(self.output_file, 1, self.samp_rate, 16)
    
    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self.update_filter()
        
    def set_transition_window(self, transition_window):
        self.transition_window = transition_window
        self.update_filter()
    
    def set_input_file(self, input_file):
        self.input_file = str(input_file)
        self.update_wav_source()
        
    def set_output_file(self, output_file):
        self.output_file = str(output_file)
        self.update_wav_sink()
