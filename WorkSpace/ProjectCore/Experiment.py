'''
EXPERIMENTCONFIG = {
    'SEED_METHOD' : ''  #using SEED_METHODS.py as source
    'PRNG_METHOD' : '', #using PRNG_METHODS.py as source
    'NUM_SETS' : '',    #generate NUM_SETS sets of length SET_LEN
    'SET_LEN': '',
    'IS_NEW_MODEL' : '',
    'PATH' : '', #if IS_NEW_MODEL, new files will be created / overidden at this location. If !IS_NEW_MODEL, previous model with weights will be loaded. File must be named
    'BATCH_SIZE': '',
    'NUM_EPOCHS': '',
    
}
'''





from typing import Dict

class Experiment:
    def __init__(self, config : Dict):
        
        self.performcount = 0
        
        for key, value in d.items():
            if value is None:
                raise ValueError(key, ' must have a value associated')
            if key == 'SEED_METHOD' || key == 'PRNG_METHOD' || key  == 'PATH':
                if not isinstance(value, str):
                    raise ValueError(key, ' must have a value type of str')
            if key == 'NUM_SETS' || key == 'SETL_LEN' || key  == 'BATCH_SIZE' || key == 'NUM_EPOCHS':
                if not isinstance(value, int):
                    raise ValueError(key, ' must have a value type of int')
            if key == 'IS_NEW_MODEL' && not isinstance(value, bool):
                raise ValueError(key, ' must have a value type of bool')
    

    def perform(self):
        self.performcount += 1
        