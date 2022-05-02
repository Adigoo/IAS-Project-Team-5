# -*- coding: utf-8 -*-
"""sample_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bn5dORdLgKWP8HXu-C9u6towEMvB6gJc
"""

import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle
import warnings
import numpy as np
warnings.filterwarnings("ignore")

def generate_data():

  # generate temperature data
  temp_data = []
  for i in range( 10000 ):
    temp = random.uniform(10, 50)
    temp_data.append( temp )

  # generate fire_alarm data
  fire_alarm_data = []
  for i in range( 10000 ):
    fire_alarm = random.randint(0,1)
    if fire_alarm == 0:
      fire_alarm_data.append( False )
    else:
      fire_alarm_data.append( True )

  return temp_data, fire_alarm_data

temp_data, fire_alarm_data = generate_data()

def create_Df( temp_data, fire_alarm_data ):
  input_data = pd.DataFrame(list(zip(temp_data, fire_alarm_data)), columns=['Temperature', 'Fire_Alarm'])
  return input_data

input_data = create_Df( temp_data, fire_alarm_data )

input_data.head()

def split_data( input_data ):
  #X = input_data.drop(columns="Fire_Alarm")
  X = input_data["Temperature"]
  
  y = input_data["Fire_Alarm"]
  
  X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80)
  return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = split_data( input_data )
print( X_train )
print( y_train )

def Decison_Tree( X_train ):
  X_train = np.array( X_train )
  X_train = X_train.reshape(-1, 1)
  decision_tree_model = DecisionTreeClassifier(max_depth =3, random_state = 42)
  decision_tree_model.fit(X_train, y_train)
  return decision_tree_model

decision_tree_model = Decison_Tree(X_train)

pickle_file = open('model.pkl', 'ab')
pickle.dump( decision_tree_model, pickle_file )
pickle_file.close()

#decision_tree_model.predict([[47.857214]])