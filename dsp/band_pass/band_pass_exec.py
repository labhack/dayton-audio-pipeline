#!/usr/bin/env python2

import sys
import os.path

from band_pass import band_pass

class band_pass_exec():
    def __init__(self, parent=None):
        self.input_file = input_file = ""
        self.low_cutoff = low_cutoff = 0
        self.high_cutoff = high_cutoff = 0
        self.transition_width = transition_width = 0
        
    def set_input_file(self, input_file):
        self.input_file = input_file
        
    def set_output_file(self, output_file):
        self.output_file = output_file
    
    def set_low_cutoff(self, cutoff):
        self.low_cutoff = cutoff
    
    def set_high_cutoff(self, cutoff):
        self.high_cutoff = cutoff
        
    def set_transition(self, width):
        self.transition_width = width
        
    def filterFile(self):
        tb = band_pass()
        tb.set_input_file(self.input_file)
        tb.set_output_file(self.output_file)
        tb.set_low_cutoff(self.low_cutoff)
        tb.set_high_cutoff(self.high_cutoff)
        tb.set_transition_width(self.transition_width)
        tb.setup_blocks()
        tb.start()
        tb.wait()
        
if __name__ == "__main__":
    myapp = band_pass_exec()
    myapp.set_input_file(str(sys.argv[1]))
    myapp.set_output_file("/audio_pipeline/dsp_results/" + os.path.basename(str(sys.argv[1])))
    myapp.set_low_cutoff(int(sys.argv[2]))
    myapp.set_high_cutoff(int(sys.argv[3]))
    myapp.set_transition(int(sys.argv[4]))
    myapp.filterFile()
    sys.exit()
