'''
#### BRIEF OVERVIEW ####
This class represents the predictive neural net, operations that can be performed on the net, and logging features
It maintains a directory at the provided path, which will log various data about the model and any training/modification
that takes place. 

If is_new_model is specified, it purges all data at the path and saves a new model.
else, it will load the model if it exists at the path specified.


#### INSTANTIATION ####
This class was made to be instantiated first. 

It has been expanded to attempt to handle non-instantiated calls, but non-instanitated interaction has not been fully tested.

NOTE on side effects: if the class is not instantiated and functions are called individually,
there will be file logging side effects that might create / overwrite files at specified paths.


#### HAVE ISSUES? ####
We have worked hard to reduce obvious bugs, but due to the ambiguity of any keras parameters being passed,
we let keras bubble up any errors that occur. If you coerce the class behavior into an unknown or bug-prone state,
please open an issue and we will handle it accordingly.
'''


import keras 
from keras.models import load_model
from keras.callbacks import CSVLogger
from keras.callbacks import ModelCheckpoint
from keras import metrics

from IPython.display import SVG, HTML
from IPython.display import display

from keras_tqdm import TQDMNotebookCallback

import numpy as np
from scipy.stats.stats import pearsonr 

import os
import shutil

import pandas as pd

class PredictiveModel:
    def __init__(self, input_width : int,  path:str, is_new_model=True, config='No Config Available'):
        self.path = path
        self.is_new_model = is_new_model # Not needed?
       
        apnd = ''
        content = ''
        if(is_new_model):
            self.model = self.CreateModel(input_width, 1)
            
            if os.path.exists(path):
                shutil.rmtree(path)
       
            os.makedirs(path)
       
            self.save_model()
        
            apnd = 'w+'
            content = 'Made New Model...\n'

        else:
            self.model = self.load_model()
            apnd = 'a+'
            content = '\n\nLoaded Model...\n'
            

        content += 'With configuration:\n' + config + '\n'
            
        with open(path + 'Model_Summary.txt', apnd) as fh:
            fh.write(content)
            # Pass the file handle in as a lambda function to make it callable
            self.model.summary(print_fn=lambda x: fh.write(x + '\n'))
            
    #Description:
    #Creates a keras sequential model based on passed params and stricly returns the keras model object.
    def CreateModel(self, input_width : int, output_width : int):
        model = keras.Sequential()
        model.add(keras.layers.Conv1D(4, 2,
                                    activation='relu',
                                    input_shape=(input_width, 1),
                                    name='conv_1'
                                 )
             )
        model.add(keras.layers.Conv1D(4, 2, activation='relu', name='conv_2'))
        model.add(keras.layers.Conv1D(4, 2, activation='relu', name='conv_3'))
        model.add(keras.layers.Conv1D(4, 2, activation='relu', name='conv_4'))
        model.add(keras.layers.MaxPool1D(1, 1, name='maxpool_1'))
        model.add(keras.layers.Dropout(0.25))
        model.add(keras.layers.Flatten(name='flatten_1'))
        model.add(keras.layers.Dense(4, activation='relu', name='dense_1'))
        model.add(keras.layers.Dense(output_width, activation='relu', name='dense_2'))    
        return model

    #Description:
    #Trains the already created neural net with passed params for training and logging 
    #(using general file i/o, ModelCheckpoint, and CsvLogger).
    #Note that Modelcheckpoint is always implemented, but parameters can be modified.
    def Train(self,
              x_train,
              y_train,
              batch_size,
              epochs,
              verbose=0,
              append=True,
              save_path=None,
              monitor='mae',
              mode='min',
              use_validation=False,
              validation_split=0.0,
              validation_data=0,
              disable_TQDMN = True 
             ):
        
        
        # Hack to fix TQDM extra lines issue...
        # Reference: https://github.com/bstriner/keras-tqdm/issues/21
        from keras_tqdm import TQDMNotebookCallback
        display(HTML("""
            <style>
                .p-Widget.jp-OutputPrompt.jp-OutputArea-prompt:empty {
                      padding: 0;
                      border: 0;
                }
            </style>
        """))
        
        
        if(save_path == None):
            save_path = self.path
            
        if(not append):
            if(os.path.isfile((save_path+'training_log.csv'))):
                open((save_path+'training_log.csv'), 'w').close()
            
        #if(enable_checkpointing):
        #perhaps allow the user to enable model checkpointing in the future (with all params) and save the model at the bottom
        checkpoint = ModelCheckpoint((save_path+'model.hd5'),
                                     monitor=monitor,
                                     verbose=verbose,
                                     save_weights_only=False,
                                     save_best_only=True,
                                     mode=mode)
        
        csv_logger = CSVLogger((save_path+'training_log.csv'), append=append, separator=',')
        
        callbacks = None
        
        if(disable_TQDMN):
            callbacks = [csv_logger, checkpoint]
        else:
            callbacks = [csv_logger, checkpoint, TQDMNotebookCallback()]
 
        history = None
        if(use_validation):
            #validation_data=validation_data is split between x and y
            history = self.model.fit(x_train,
                                     y_train,
                                     batch_size=batch_size,
                                     epochs=epochs,
                                     validation_split=validation_split,
                                     verbose=verbose,
                                     callbacks=callbacks)
        else:
            history = self.model.fit(x_train,
                                     y_train,
                                     batch_size=batch_size,
                                     epochs=epochs,
                                     verbose=verbose,
                                     callbacks=callbacks)
        
        return history
        
    #Description:
    #Evaluates model baed on test data passed in, performs logging, and returns the prediction results.
    def Predict(self, x_test,y_test,append=True,save_path=None):
        if(save_path == None):
            save_path = self.path
            
        if(not append):
            if(os.path.isfile((save_path+'test_results.csv'))):
                open((save_path+'test_results.csv'), 'w').close()
            
        y_pred = self.model.predict(x_test)
        #f=open((save_path+'test_results.csv'),'ab')
        
        y_pred = y_pred.flatten()
        pearsoncorr = pearsonr(y_test,y_pred) # y_actual and y_pred
        pearsoncorr = np.array(pearsoncorr)
        
        #np.savetxt(f, pearsoncorr, header="pearsoncorr", delimiter=",")
        
        
        df = pd.DataFrame({"y_test" : y_test,
                           "y_pred" : y_pred,
                           "Pearson Co. For Entire Data Set (Not individual)": pearsoncorr[0],
                           "P-Value for Pco": pearsoncorr[1]})
        
        #csvlogger apparently not supported with model.predict... have to do it manually (/externally).
        df.to_csv(save_path + "test_results.csv", index=False,mode="a")
        
        #np.savetxt(f, np.c_[y_test,y_pred], header="y_test,y_pred", delimiter=",")
        #np.savetxt(f, y_test, header="y_test", delimiter=",")
        
        if(os.path.isfile((save_path+'Model_Summary.txt'))):
            content = "Pearson Correlation Coefficient:" + str(pearsoncorr[0]) + '\n'
            content += "2-tailed p-value:                "+ str(pearsoncorr[1]) + '\n'
        
            with open(save_path + 'Model_Summary.txt', 'a+') as fh:
                fh.write(content)
        
        return y_pred
    
    #Description:
    #Complies the model using keras.model.compile with passed parameters. 
    #Note that Nadam is hardcoded for now in order to pass learning rate.
    def Compile(self, loss:str , lr:float):
        self.model.compile(loss=loss, optimizer=keras.optimizers.Nadam(learning_rate=lr),metrics=['mae'])
        
    #Description:
    #saves full model based on path provided
    def save_model(self, path=None):
        if(path == None):
            path = self.path
        self.model.save(path + 'model.hd5')

    #Description:
    #loads full model based on path provided
    def load_model(self, path=None):
        if(path == None):
            path = self.path
        # returns a compiled model
        # identical to the previous one
        return load_model(path + 'model.hd5')
        
        

