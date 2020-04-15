'''
#### BRIEF OVERVIEW ####
This class is responsible for generating specified data, creating training and testing sets, normalizing data, and shaping data. 

#### INSTANTIATION ####
Requires instantiation

#### HAVE ISSUES? ####
We have worked hard to reduce obvious bugs, but if you coerce the class behavior into an unknown or bug-prone state,
please open an issue and we will handle it accordingly.

'''



# custom tooling for seeding and PRNG
import Core.PrngMethods
import Core.SeedMethods 

import numpy as np

# for data normalization
from sklearn import preprocessing

class DataBroker:
    def __init__(self, NUM_SETS : int, SET_LEN: int, PRNG_METHOD : str, SEED_METHOD: str):
        self.prng_method = PRNG_METHOD
        self.seed_method = SEED_METHOD
        
        # Generation Parameters: Generate y sets of length z
        self.numsets = NUM_SETS
        self.setlength = SET_LEN

        # train and test data inits
        self.x_train = []
        self.y_train = []

        self.x_test = []
        self.y_test = []
        
        #### set up training data: ####
        self.aggregate_and_split(self.x_train, self.y_train, 2)
        
        #### set up testing data: ####
        self.aggregate_and_split(self.x_test, self.y_test, 4)
        

    # Description:
    # This function invokes the PRNG and obtains y sets of length z. 
    # Each set has its own seed, obtained from our custom SeedGenerator
    # It then splices the last number in a set off and appends
    # n-1 to x (for x_train or test) and the nth to y (for y_train or test)
    # Params:
    # x: gets the first n-1 values of each set
    # y: gets the nth value of the set
    # numsets: represents the amount of sets
    # setlength: represents length of each set
    def aggregate_and_split(self, x, y, t):
        temp = []
       
        for i in range(self.numsets):
            t = getattr(Core.SeedMethods, self.seed_method)(t)
            temp = getattr(Core.PrngMethods, self.prng_method)(t,self.setlength)
            #print(temp, 'and', self.setlength, end = '<->')
            #print(t, end = ' ')
            for a in range(len(temp)): #little expensive
                temp[a] = int(temp[a])
            
            n = temp[-1]
            y.append(n)
            x.append(temp[:-1])
             
    def normalize_input_data(self,x):
        #normalize data to prevent weight values overflowing (NaN) and convert to np.array
        x = preprocessing.normalize(np.array(x))
        
    def normalize_target_data(self,y):
        y= preprocessing.normalize(np.array([y]))
        y = y.flatten() #ravel will be more efficient if we don't need to modify.
        
    def reshape_input_data(self):
        self.x_train = self.x_train.reshape(self.x_train.shape[0], self.x_train.shape[1], 1)
        self.x_test = self.x_test.reshape(self.x_test.shape[0], self.x_test.shape[1], 1)
        
    def shape_and_normalize(self):
        
        #normalize data to prevent weight values overflowing (NaN) and convert to np.array
        self.x_train = preprocessing.normalize(np.array(self.x_train))
        self.y_train = preprocessing.normalize(np.array([self.y_train]))
        self.y_train = self.y_train.flatten() #ravel will be more efficient if we don't need to modify.
        
        
        #normalize data to prevent weight values overflowing (NaN) and convert to np.array
        self.x_test = preprocessing.normalize(np.array(self.x_test))
        self.y_test = preprocessing.normalize(np.array([self.y_test]))
        self.y_test = self.y_test.flatten() #ravel will be more efficient if we don't need to modify.
        
        self.reshape_input_data()
        
    def print_all_shapes(self):
        print('x_train', self.x_train.shape)
        print('y_train', self.y_train.shape)

        print('x_test', self.x_test.shape)
        print('y_test', self.y_test.shape)    
    
    def print_n_values(self):
        pass
