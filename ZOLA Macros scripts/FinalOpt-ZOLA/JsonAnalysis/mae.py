#Compute, collect, compare, and analyze ARE, MSE, MAE, and WaveFrontError.
from LightPipes import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
import math
import random
import numpy as np
import os
import pandas as pd

filename="bench"
pred=np.load(filename+".npy")
gt=np.load("gt.npy")
Metrics=[]
# Initialize and start main control loop
runMax=len(pred)
for runCount in range(0,runMax): 
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

print("MAE(Zs) Bench:%f"%(AvgMAE))
'''
Metrics.sort(key=lambda x:x[0])
Metrics_np = np.array(Metrics)
np.save(filename+"_Metrics.npy",Metrics_np)
'''

filename="gaussian"
pred=np.load(filename+".npy")
gt=np.load("gt.npy")
Metrics=[]
# Initialize and start main control loop
runMax=len(pred)
for runCount in range(0,runMax): 
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

print("MAE(Zs) Gaussian:%f"%(AvgMAE))
'''
Metrics.sort(key=lambda x:x[0])
Metrics_np = np.array(Metrics)
np.save(filename+"_Metrics.npy",Metrics_np)
'''

filename="tear"
pred=np.load(filename+".npy")
gt=np.load("gt.npy")
Metrics=[]
# Initialize and start main control loop
runMax=len(pred)
for runCount in range(0,runMax): 
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

print("MAE(Zs) Tear:%f"%(AvgMAE))
'''
Metrics.sort(key=lambda x:x[0])
Metrics_np = np.array(Metrics)
np.save(filename+"_Metrics.npy",Metrics_np)
'''

filename="rec"
pred=np.load(filename+".npy")
gt=np.load("gt.npy")
Metrics=[]
# Initialize and start main control loop
runMax=len(pred)
for runCount in range(0,runMax): 
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

print("MAE(Zs) Rec:%f"%(AvgMAE))
'''
Metrics.sort(key=lambda x:x[0])
Metrics_np = np.array(Metrics)
np.save(filename+"_Metrics.npy",Metrics_np)
'''

filename="hat"
pred=np.load(filename+".npy")
gt=np.load("gt.npy")
Metrics=[]
# Initialize and start main control loop
runMax=len(pred)
for runCount in range(0,runMax): 
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

print("MAE(Zs) Hat:%f"%(AvgMAE))
'''
Metrics.sort(key=lambda x:x[0])
Metrics_np = np.array(Metrics)
np.save(filename+"_Metrics.npy",Metrics_np)
'''

filename="ring"
pred=np.load(filename+".npy")
gt=np.load("gt.npy")
Metrics=[]
# Initialize and start main control loop
runMax=len(pred)
for runCount in range(0,runMax): 
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

print("MAE(Zs) Ring:%f"%(AvgMAE))
'''
Metrics.sort(key=lambda x:x[0])
Metrics_np = np.array(Metrics)
np.save(filename+"_Metrics.npy",Metrics_np)
'''