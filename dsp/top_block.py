#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat May 21 18:02:22 2016
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 16000
        self.low_freq = low_freq = 1000
        self.high_freq = high_freq = 4000
        self.input_file = input_file = "NULL"
        
    def setup_blocks(self):
        ##################################################
        # Blocks
        ##################################################
        self.update_input()
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink("/home/bward/Documents/Labhack 2016/Cleaned Audio/cleaned_audio.wav", 1, self.samp_rate, 16)
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, self.samp_rate, self.low_freq, self.high_freq, 10, firdes.WIN_HAMMING, 6.76))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_wavfile_sink_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0, 0))    


    def get_samp_rate(self):
        return self.samp_rate

    def update_filter(self):
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.low_freq, self.high_freq, 10, firdes.WIN_HAMMING, 6.76))
    
    def update_input(self):
        self.blocks_wavfile_source_0 = blocks.wavfile_source(self.input_file, False)

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.update_filter()
        
    def set_low_freq(self, low_freq):
        self.low_freq = low_freq
        self.update_filter()
        
    def set_high_freq(self, high_freq):
        self.high_freq = high_freq
        self.update_filter()

    def set_input_file(self, input_file):
        print("Setting file: ", str(input_file))
        self.input_file = str(input_file)
        self.update_input()
        
if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()
