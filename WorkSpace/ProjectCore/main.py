import sys
from Core.Experiment import Experiment
from Core.PrngMethods import Get_Defs


def main():  
    
    
    ''' Attempt at accepting a configuration file
    fn = sys.argv[1]
    if not os.path.exists(fn):
        print("Must provide a filepath to configuration file. For an example configuration, see Core/experiment.py\n")
        return
    
    data = ''
    with open(fn, 'r') as file:
        data = file.read().replace('\n', '')   
        
    print(data)
    
    
    json_acceptable_string = data.replace("'", "\"")
    
    config = json.loads(json_acceptable_string)
    
    '''
    defs = Get_Defs()
    print('Prng defs: ',defs)
 
    configuration = {
        'DISABLE_TQDMN' : True,
        'VERBOSE' : 0,
        'LOUD_LOGGING': False,
    
        'IS_NEW_MODEL' : True,
        'PATH' : './Middle_Square_Secondary/',
        'SEED_METHOD' : 'ticks',               
        'PRNG_METHOD' : 'Middle_Square',       
        'NUM_SETS' : 1000,                     
        'SET_LEN': 2000,                                               
        'BATCH_SIZE': 15,
        'NUM_EPOCHS': 5,
        
        'CHKPNT_MONITOR' : 'mae',
        'CHKPNT_MODE' : 'min',
        
        
        'USE_VALIDATION' : True ,
        'VALIDATION_SPLIT' :  0.2,
    
        'OVERRIDE_LOAD_COMPILATION' : False,
        'LR': .001,
        'LOSS_METHOD':'mean_absolute_error' #mae
    }  


    E = Experiment(configuration)
    E.perform()
   
    
         
        
if __name__ == "__main__":
    main()