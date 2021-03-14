import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import json 
import numpy  as np
from random import random,seed
from keras.models  import Sequential,load_model

seed(1)

class ModelOne():

    def __init__(self, config_file):
        
        with open(config_file) as json_file:
            data_config = json.load(json_file)
            model_path  = data_config["config"]["model_path"]
            self.__model   = load_model(model_path)        

    def predict(self, input):        
        np_input = np.array(input)
        prediction = self.__model.predict(np_input.reshape(1,8))        
        return prediction

def create_model_one(config_file):
    return  ModelOne(config_file)


if __name__ == '__main__':    
    model = ModelOne('config.json')
    prediction = model.predict([1,2,3,4,5,6,7,8])
    print(prediction)
    