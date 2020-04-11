import keras 
from keras.models import load_model
from keras.callbacks import CSVLogger
import os

# fancy arrays
import numpy as np

# For Regression Analysis
from scipy.stats.stats import pearsonr 

# for file removal
import shutil

class PredictiveModel:
    def __init__(self, input_width : int,  path:str, is_new_model=True):
        self.path = path
        self.is_new_model = is_new_model
       
        
        
        if(is_new_model):
            self.model = self.CreateModel(input_width, 1)
        else:
            self.model = self.load_model()
            

        if os.path.exists(path):
            shutil.rmtree(path)
        
        os.makedirs(path)
            
        with open(path + 'Model_Summary.txt','w+') as fh:
            # Pass the file handle in as a lambda function to make it callable
            self.model.summary(print_fn=lambda x: fh.write(x + '\n'))
            
             
    # Description:
    # This function sets up the model and returns a keras sequential model.
    # Params:
    # input_width: the size of the input layer
    # output_width: the size of the output layer
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


    def Train(self,
              x_train: list,
              y_train: list,
              batch_size: int,
              epochs: int,
              verbose=0,
              append=True,
              save_path=None,
              use_validation=False,
              validation_split=0.0,
              validation_data=0
             ):
        if(save_path == None):
            save_path = self.path
            
        csv_logger = CSVLogger((save_path+'training_log.csv'), append=append, separator=',')
        
        history = None
        if(use_validation):
            history = self.model.fit(x_train,y_train,batch_size=batch_size,epochs=epochs,validation_split=validation_split,verbose=verbose, 
            validation_data=validation_data, callbacks=[csv_logger])
        else:
            history = self.model.fit(x_train,y_train,batch_size=batch_size,epochs=epochs,verbose=verbose, callbacks=[csv_logger])
        
        self.save_model(save_path)
        
        return history
        
    def Predict(self, x_test,y_test,append=True,save_path=None):
        if(save_path == None):
            save_path = self.path
            
        if(not append):
            open((save_path+'test_results.csv'), 'w').close()
            
        y_pred = self.model.predict(x_test)
        f=open((save_path+'test_results.csv'),'ab')
        
        y_pred = y_pred.flatten()
        pearsoncorr = pearsonr(y_test,y_pred) # y_actual and y_pred
        pearsoncorr = np.array(pearsoncorr)
        
        np.savetxt(f, pearsoncorr, header="pearsoncorr", delimiter=",")
        
        np.savetxt(f, y_pred, header="y_pred", delimiter=",")
        np.savetxt(f, y_test, header="y_test", delimiter=",")
        
        #print("Pearson Correlation Coefficient:", pearsoncorr[0])
        #print("2-tailed p-value:                ", pearsoncorr[1])
        #csvlogger apparently not supported with model.predict... have to do it manually.
        
        return y_pred
    
    def Compile(self, loss:str , lr:float):
        self.model.compile(loss=loss, optimizer=keras.optimizers.Nadam(learning_rate=lr))
        
    def save_model(self, path=None):
        if(path == None):
            path = self.path
        self.model.save(path + 'model.h5')  # creates a HDF5 file 'model.h5'

    def load_model(self, path=None):
        if(path == None):
            path = self.path
        # returns a compiled model
        # identical to the previous one
        return load_model(path + 'model.h5')
        
        

