import os
import json 
#import pandas as pd
import numpy  as np
from random import random,seed
seed(1)

class Models():

	def __init__(self,config_path):
		self.output      = 0
		self.comment     = ''
		with open(config_path) as json_file:
			data_config       = json.load(json_file)
		self.model_path   = data_config["config"]["model_path"] 
	
	def validation(self,myinput):
		if not type(myinput).__name__=='list':
			self.output =9999999
			self.comment='Invalid'
			raise TypeError("Only list allowed")
			
		if len(myinput)<8:
			self.output=9999999
			self.comment='Invalid'
			raise Exception("the list must include 8 numbers")
		else:
			for n in myinput:
				if not (type(n).__name__=='int' or type(n).__name__=='float'):
					raise Exception("the list must include 8 whole numbers or decimals")
					self.output=9999999
					self.comment='Invalid'
		self.myinput = np.array(myinput)
	
	def gmm_model(self):
		from keras.models          import Sequential,load_model
		model_path   = self.model_path
		myinput      = self.myinput

		if not os.path.isfile(model_path):
			self.comment='path not found'
			raise Exception('path not found')
		
		modelfrom    = 'k'
		self.model   = load_model(model_path)
		self.output  = self.dopredict(myinput)[0][0]
		#self.output = random()
		self.comment = "Done!"
		print(self.output)

	def gmb_model(self):
		#from sklearn.neighbors     import KNeighborsRegressor
		model_path   = self.model_path
		modelfrom    ='sl'
		self.output  = random()
		self.comment = "Done!"
		print(self.output)
	
	def dopredict(self,myinput=None):
		prediction = self.model.predict(myinput.reshape(1,8))
		return(prediction)


if __name__ == "__main__":
	myinput=[1.,2,2,3,4,5,6.,7]
	json_path='config.json'
	m=Models(json_path)
	m.validation(myinput=myinput)
	m.gmm_model()
	#m.gmb_model()
