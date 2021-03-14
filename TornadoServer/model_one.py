import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import json 
import numpy  as np
from random import random,seed
seed(1)

class ModelOne():

    def __init__(self, model_path):        
        from keras.models  import Sequential,load_model
        self.model   = load_model(model_path)        

    def predict(self, input):        
        np_input = np.array(input)
        prediction = self.model.predict(np_input.reshape(1,8))        
        return prediction

def get_version():
    return sys.version

def create_model_one(model_path):
    return  ModelOne(model_path)


if __name__ == '__main__':
    print( get_version())
    model = ModelOne('gmm0.9.hdf5')
    prediction = model.predict([1,2,3,4,5,6,7,8])
    print(prediction)
    