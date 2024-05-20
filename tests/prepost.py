#!/usr/bin/env python3

"""Tests uuts prepost transient shot"""

from acq400_regression.tests.generic import generic
from acq400_regression.misc import tri

from acq400_hapi import PR, pprint, pv #remove me after testing


class Prepost(generic):
    test_type = "prepost"
    
    triggers = [
        [1,0,0],
        [1,0,1],
        [1,1,1],
    ]

    pre = 50000
    post = 50000

    dir_fmt = "{type}_trg{trigger}_evt{event}"
    
    def parser(parser):
        print(f"prepost argparser here")
        
    def run(self):
        self.post = self.args.post if self.args.post else self.post
        self.save_state('post', self.post)
        
        self.pre = self.args.pre if self.args.pre else self.pre
        self.save_state('pre', self.pre)
        
        self.wavelength = self.args.divisor
        
        freq, voltage = self.get_freq_and_voltage()

        for trigger in self.get_trigger():
            for event in self.get_event():

                self.siggen.config_params(freq, voltage)
                self.siggen.config_trigger(trigger, self.args.cycles)

                self.run_iters(trigger, event)
                
                if self.args.save: self.th.save_test()
                self.th.stash_results()
                
        self.log.info(f"[{self.th.testname.title()}] Test Completed")
        
    #@generic.catch_error
    def run_iters(self, trigger, event):
        for run in self.get_run():
            self.log.info(f"[{self.test_type}] Trigger {trigger} Event {event}")
            
            results = []

            self.uuts.abort()

            self.uuts.transient(pre=self.pre, post=self.post, trg=trigger, evt=event)

            self.uuts.arm()
            self.log.info('Arming')

            self.uuts.wait_armed(timeout=45)
            self.log.info('Ready')

            if tri(trigger, 'source') != 1: self.siggen.trigger(delay=1)

            self.uuts.wait_pre_complete(2 * self.pre)

            if tri(event, 'source') != 1: self.siggen.trigger()

            self.uuts.wait_completed(timeout=60)
            self.log.info('Completed')

            dataset = self.th.offload_dataset()
            
            ideal_wave, tolerance, dtype = self.get_ideal_wave(dataset, self.is_soft(trigger), self.is_rising(event))
            
            results.append(self.check_wave_synchronous(dataset, ideal_wave, tolerance))

            if not self.check_passed(results): break
        
        self.log.info(f"All runs complete {run}/{self.args.runs}")