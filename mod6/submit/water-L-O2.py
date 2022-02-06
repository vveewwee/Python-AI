import pandas as pd
import numpy as np
import csv
from maxi_neurone import Neurone, mean_squared_error, linear_activation

DATA = ["RAD","02"]
X_DATA = ["RAD"]
Y_DATA = ["02"]
LR = 0.00001 #sensible

def getData() :
   train = np.read_csv("./data/train.csv")
   x_train = np.array(train["x_train"])
   y_train = np.array(train["y_train"])
   test = np.read_csv("./data/test.csv")
   x_test = np.array(test["x_test"])
   y_test = np.array(test["y_test"])
   return (x_train, y_train), (x_test, y_test)

def batch_me(data, batch_size):
   #Need Some Code
      yield #Need Some Code

if __name__=='__main__':
   #Need Some Code


