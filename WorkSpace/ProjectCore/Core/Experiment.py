# for Controlled PRN generation
from Core.DataBroker import DataBroker

from Core.PredictiveModel import PredictiveModel

# abstracted to logging eventually
from scipy.stats.stats import pearsonr 
# Plotting
import matplotlib.pyplot as plt


class Experiment:
    def __init__(self, config : dict):
        self.pred = None
        self.db = None
        self.config = config
        
        self.performcount = 0
        #to do: > 0 checks
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

    def perform(self):
        self.performcount += 1
        
        #generate training and testing data
        print('\nGenerating', self.config['NUM_SETS'], 'sets of',self.config['SET_LEN'], 'using', self.config['PRNG_METHOD'], '...')
        
        self.db = DataBroker(self.config['NUM_SETS'],
                         self.config['SET_LEN'],
                         self.config['PRNG_METHOD'],
                         self.config['SEED_METHOD'])
        
        print("\nGeneration Successful!")
        print("\nNormalizing and shaping data for training...")
        
        self.db.shape_and_normalize()
        
        print("\nTraining and testing sets were successfully generated with input and target data...\n")
        
        self.db.print_all_shapes()
        
        print("\nPrinting Model Summary...\n")
        
        self.pred = PredictiveModel(self.db.x_train.shape[1])
        
        self.pred.model.summary()
        
        print("\nInitializing Training...\n")
        
        self.pred.Compile('mean_squared_error', 'adam')
        
        #todo: implement logging class for storing results and generating graphs.
        
        history = self.pred.Train(self.db.x_train, self.db.y_train, self.config['BATCH_SIZE'], self.config['NUM_EPOCHS'], 1)
        
        
        
        y_pred = self.pred.Predict(self.db.x_test)
        y_actual = self.db.y_test

        plt.plot(y_actual, color = 'red', label = 'Target Data')
        plt.plot(y_pred, color = 'blue', label = 'Predicted Data')
        plt.title('Prediction')
        plt.legend()
        plt.show()

        y_pred = y_pred.flatten()

        print(y_actual)
        print(y_pred)
        print(y_actual.shape)
        print(y_pred.shape)

        pearsoncorr = pearsonr(y_actual,y_pred)
        print("Pearson Correlation Coefficient:", pearsoncorr[0])
        print("2-tailed p-value:                ", pearsoncorr[1])
        
'''
    
# Visualization
from IPython.display import SVG 
from IPython.display import display
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model

    
    
    
'''