#!/usr/bin/env python3

"""Tests uuts streaming"""

from acq400_regression.tests.generic import generic
from acq400_regression.misc import tri, ifnotset

from acq400_hapi import PR, pprint, AcqPorts#remove me after testing
import numpy as np
from matplotlib import pyplot as plt


class Stream(generic):
    test_type = "stream"

    dir_fmt = "{type}_{runtime}s"
    
    runtime = 30
    
    def get_args(parser):
        parser.add_argument('--runtime', default=30, type=int, help=f"stream runtime")
        return parser

    def run(self):
        self.runtime = ifnotset(self.args.runtime, self.runtime)
        self.save_state('runtime', self.runtime)
        self.wavelength = self.args.divisor #add into args
        
        freq, voltage = self.get_freq_and_voltage()
        self.siggen.config_params(freq, voltage)
        self.siggen.config_contiguous()
        self.uuts.setup(trg='1,0,1')

        self.run_iters()
        
        if self.args.save: self.th.save_test()
        self.th.stash_results()
        
        self.log.info(f"[{self.th.testname.title()}] Test Completed")
        
    def run_iters(self):
        
        for run in self.get_run():
            results = []
            self.uuts.abort()
            self.uuts.stream_to_host()
            dataset = self.th.import_dataset('HOST')
            results.append(self.check_spad(dataset))
            
            if not self.check_passed(results): break
        self.log.info(f"All runs complete {self.run}/{self.runs}") 
            
if __name__ == '__main__':
    print('running stream')
    from acq400_regression import Test_Handler
    
    #add args?
    #import regressin test handelr
    #parser args
    #set test
    #run test
    
    
    
    """
    1)
    from main
    
    th = TH() no args?
    th.parser_args()
    th.run_tests(th.args.tests)
    
    from single test
    
    th = TH()
    th.parser_args()
    th.run_tests(stream)
    
    2)
    from main
    
    args = TH.parser_args() can be passed in 
    th = TH(args)
    th.run_tests()
    
    
    
    
    
    """