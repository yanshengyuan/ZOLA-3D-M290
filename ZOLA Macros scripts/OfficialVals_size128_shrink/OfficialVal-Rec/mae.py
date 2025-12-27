#Compute, collect, compare, and analyze ARE, MSE, MAE, and WaveFrontError.
from LightPipes import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
import math
import random
import configparser
import numpy as np
from UserFunctions.UserFunctions import SmoothStep
from UserFunctions.UserFunctions import SmoothCircAperture
import os
import pandas as pd

filename="rec"


pred=np.load(filename+".npy")
gt=np.load("gt.npy")
Metrics=[]
# Initialize and start main control loop
runMax=len(pred)
for runCount in range(0,runMax):
    print(runCount)   

    
    zernikecoefficients = pred[runCount]
    zGT = gt[runCount]

    mae = 0.0
    for x in range(len(zGT)):
        mae += abs(zernikecoefficients[x]-zGT[x])
    mae = mae/len(zGT)
    Metrics.append([mae, runCount])

AvgMAE=0.0
for i in range(len(Metrics)):
    AvgMAE+=Metrics[i][0]
AvgMAE=AvgMAE/len(Metrics)

print("MAE(zernike coefficients):%f"%(AvgMAE))

Metrics.sort(key=lambda x:x[0])
Metrics_np = np.array(Metrics)
np.save(filename+"_Metrics.npy",Metrics_np)