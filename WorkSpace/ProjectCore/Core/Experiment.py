'''
#### BRIEF OVERVIEW ####
This class interfaces with the DataBroker and the PredictiveModel to perform the experiment.
It also contains logging methods of its own. It accepts a configuration file based on the
below usage to control the experiment.

#### INSTANTIATION ####
Requires instantiation

#### HAVE ISSUES? ####
We have worked hard to reduce obvious bugs, but due to the ambiguity of any keras parameters being passed,
we let keras bubble up any errors that occur. If you coerce the class behavior into an unknown or bug-prone state,
please open an issue and we will handle it accordingly.

## example usage ##    
configuration = {
        'DISABLE_TQDMN' : True,             #Shortened pretty output for epoch results. Disable if executing from cli.
        'LOUD_LOGGING': False,              #Extra output detailing exactly what the experiment is doing at all times.
        'VERBOSE' : 0,                      #if training output (model.fit) is verbose
        'IS_NEW_MODEL' : False,             #Whether to load a previous model or not... ->
        'PATH' : './Middle_Square/',        #if IS_NEW_MODEL, new files will be created / overidden at PATH. ... 
                                            #If !IS_NEW_MODEL, previous model with weights will be loaded at PATH. 
        
        'SEED_METHOD' : 'ticks',            #using Core.SeedMethods as source   
        'PRNG_METHOD' : 'Middle_Square',    #using Core.PrngMethods as source  
        'NUM_SETS' : 1000,                  #generate NUM_SETS sets 
        'SET_LEN': 2000,                    #of length SET_LEN                        
        
        'USE_VALIDATION' : True ,           #use a portion of input data to fine tune nn architecture
        'VALIDATION_SPLIT' :  0.2,          #split training data between training and validation
        'BATCH_SIZE': 15,                   #size of batch, determined by how many segmented training samples (NUM_SETS) in each epoch.
        'NUM_EPOCHS': 1,                    #number of forward passses and one backward passses through of all the training input data.
        
        'CHKPNT_MONITOR' : 'mae',            #model checkpoint is implemented, which saves the model after each epoch if the ->
        'CHKPNT_MODE' : 'min',               #CHKPOINT_MONITOR metric is CHKPNT_MODE (minimized or maximized).
        
       
        
    
        'OVERRIDE_LOAD_COMPILATION' : False,  #if IS_NEW_MODEL == false, a previous model will be loaded from the PATH. By default, 
                                              #keras compiles the loaded model on load using the saved training configuration, 
                                              #so if you want to specify a new learning rate or loss method to track, you will have to
                                              #set this flag to override the compilation.
        'LR': .001,
        'LOSS_METHOD':'mean_squared_error'
        
        
    }  
    
    #note: *** deprecated *** 'OPTIMIZER_METHOD' : 'adam' ### currently hardcoded with Nadam to pass in learning rate.

'''


from Core.DataBroker import DataBroker
from Core.PredictiveModel import PredictiveModel

from scipy.stats.stats import pearsonr 
import matplotlib.pyplot as plt

import os

class Experiment:
    def __init__(self, config : dict):
        self.pred = None
        self.db = None
        self.config = config
        self.path = self.config['PATH']
        self.performcount = 0
        
        ''' TODO: Implement type and value checks
        #value checks are mainly > 0 checks
        for key, value in self.config.items():
            if value is None:
                raise ValueError(key, ' must have a value associated')
            if key == 'SEED_METHOD' or key == 'PRNG_METHOD' or key  == 'PATH':
                if not isinstance(value, str):
                    raise ValueError(key, ' must have a value type of str')
            if key == 'NUM_SETS' or key == 'SET_LEN' or key  == 'BATCH_SIZE' or key == 'NUM_EPOCHS':
                if not isinstance(value, int):
                    raise ValueError(key, ' must have a value type of int')
            if key == 'IS_NEW_MODEL' and not isinstance(value, bool):
                raise ValueError(key, ' must have a value type of bool')
        '''
    #Description:
    #Executes experiment
    def perform(self):
        print("\n**********",self.config['PRNG_METHOD'],"Experiment Initiated**********")
        
        self.performcount += 1
        loud_logging = self.config['LOUD_LOGGING']
        
        
        
        ### extra logging
        if(loud_logging):
            
            print("\nConfiguration settings accepted:", self.config)
            
            print('\nGenerating',
                  self.config['NUM_SETS'],
                  'sets of',
                  self.config['SET_LEN'],
                  'using',
                  self.config['PRNG_METHOD'], '...')
        
        ### Instantitate the Databroker, which handles number generation, normalization, and shaping.
        self.db = DataBroker(self.config['NUM_SETS'],
                         self.config['SET_LEN'],
                         self.config['PRNG_METHOD'],
                         self.config['SEED_METHOD'])
        
        ### extra logging
        if(loud_logging):
            print("\nGeneration Successful!")
            print("\nNormalizing and shaping data for training...")
        
        ### Instantiated generated the data, now its time to shape and normalize.
        self.db.shape_and_normalize()
        
        ### extra logging
        if(loud_logging):
            print("\nTraining and testing sets were successfully generated with input and target data...\n")
            self.db.print_all_shapes()
            print("\nPrinting Model Summary...\n")
        
        ### Instantiate predictive model.
        self.pred = PredictiveModel(self.db.x_train.shape[1],self.config['PATH'],self.config['IS_NEW_MODEL'],str(self.config))
        
        ### extra logging
        if(loud_logging):
            self.pred.model.summary()
            print("\nInitiate Training...\n")
        
        ### since model_load also compiles the model, we give user opportunity to override the compilation
        if(self.config['IS_NEW_MODEL'] or self.config['OVERRIDE_LOAD_COMPILATION']):
            self.pred.Compile(self.config['LOSS_METHOD'],self.config['LR'])
        
        ### train the model.
        history = self.pred.Train(self.db.x_train,
                                  self.db.y_train,
                                  self.config['BATCH_SIZE'],
                                  self.config['NUM_EPOCHS'],
                                  self.config['VERBOSE'],
                                  monitor=self.config['CHKPNT_MONITOR'],
                                  mode=self.config['CHKPNT_MODE'],
                                  use_validation=self.config['USE_VALIDATION'],
                                  validation_split=self.config['VALIDATION_SPLIT'],
                                  disable_TQDMN = self.config['DISABLE_TQDMN']
                                  )
        
        
        
        if(loud_logging):
            print("Training Finished!\n\nPrinting results...\n")
            print("History Keys: ", history.history.keys())
        
        
        ### summarize history for loss ###
        
        # Note: if monitoring two metrics that are the same for checkpointing and training, you only need to display 'loss', which keras returns by default. 
        # Otherwise if you want to see the metric associated with checkpoint monitor loss, you need to add that to the graph. Also note thatit might be advisable 
        # to create two graphs for the latter, because different loss functions interpret loss differently, possibly not allowing you to see scaled plots correctly. 
        # you will have to add those accordingly. See print(history.history.keys())
        plt.plot(history.history['loss'], label = 'loss')
        plt.plot(history.history['val_loss'], label = 'validation_loss')
        plt.legend()
        #plt.plot(history.history['mae'])
        #plt.plot(history.history['val_mae'])
        plt.title('Loss Plot From Training\n')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        #plt.legend(['loss', 'validation_loss',], loc='upper left') #'train_mae', 'test_mae'
          
        i = 0
        while True:
            i += 1
            newname = '{}{:d}.png'.format('Train_LossPlot', i)
            if os.path.exists(newname):
                continue
            plt.savefig(self.path + newname)
            break
        
        plt.show()
        
        
                  
        ### summarize prediction data for regression analysis ###
                  
        y_pred = self.pred.Predict(self.db.x_test, self.db.y_test)
        y_actual = self.db.y_test

        plt.plot(y_actual, color = 'red', label = 'Target Data')
        plt.plot(y_pred, color = 'blue', label = 'Predicted Data')
        plt.legend()
        plt.title('Correlation Plot From Testing\n')
        plt.ylabel('Normalized PRN (Blue is Predicted ... Red is Target)')
        plt.xlabel('Sequential Prediction Index (from 0 to Num_SETs - 1)')
        
        y_pred = y_pred.flatten() #flatten y_pred to for PCC calculation to include in title

        #print(y_actual)
        #print(y_pred)
        #print(y_actual.shape)
        #print(y_pred.shape)

        pearsoncorr = pearsonr(y_actual,y_pred)
        
        plt.title('Prediction\n' + "Pearson Correlation Coefficient: "+ str(pearsoncorr[0]) +"\n2-tailed p-value: " + str(pearsoncorr[1]) )
        
        i = 0
        while True:
            i += 1
            newname = '{}{:d}.png'.format('Test_RegressionPlot', i)
            if os.path.exists(newname):
                continue
            plt.savefig(self.path + newname)
            break
        
        plt.show()
        
        print("\nPearson Correlation Coefficient:", pearsoncorr[0])
        print("2-tailed p-value:                ", pearsoncorr[1] , '\n')
        
        print("Finished training, testing, and logging. Files saved to" , self.config['PATH'], '\n')
        
    
        print('**********',self.config['PRNG_METHOD'],'finished**********')
        
