import sys
import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import json 
#import pandas as pd
import numpy  as np
from random import random,seed
seed(1)

class Models():

    def __init__(self, model_path):        
        from keras.models  import Sequential,load_model
        self.model   = load_model(model_path)        

    def predict(self, input):        
        np_input = np.array(input)
        prediction = self.model.predict(np_input.reshape(1,8))        
        return prediction



def get_sys_path():
    import sys
    return sys.path

def calculate_area(width, height):
    return width*height

def get_result_with_comment(area):
    comment=""
    if area<100 :
       comment= "area<100"
    elif area < 1000:
       comment= "area>=100 && area <1000 "
    elif area < 10000:
       comment= "area>=1000 && area <10000 "
    else:
       comment= "area>=10000"
    return {"value":area, "comment":comment} 

def calculate_area_and_comment(width, height):
   
    area=  width*height    
    return get_result_with_comment(area)
    

def get_version():
    return sys.version


def create_model(model_path):
    return Models(model_path)

def predict(model, input):
    print(input)
    model.predict(input)


if __name__ == '__main__':
    print( get_version())
    model = Models('gmm0.9.hdf5')
    prediction = model.predict([1,2,3,4,5,6,7,8])
    print(prediction)
    