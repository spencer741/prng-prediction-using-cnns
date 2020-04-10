
import keras 

class PredictiveModel:
    def __init__(self, input_width : int ):
    
       self.model = self.CreateModel(input_width, 1)
        
        
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


    def Train(self, x_train: list, y_train : list , batch_size : int, epochs : int, verbose:int):
        #history=mod.fit(x_train,y_train,batch_size=batch_size,epochs=epochs, validation_split=0.1,verbose=1, 
        #validation_data=(x_test, y_test))
        return self.model.fit(x_train,y_train,batch_size=batch_size,epochs=epochs,verbose=verbose)
    
    def Predict(self, x_test):
        return self.model.predict(x_test)
    
    def Compile(self, loss:str , optimizer:str):
        self.model.compile(loss=loss, optimizer=optimizer)
        
        