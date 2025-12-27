import numpy as np

data=np.load('gaussian_Metrics.npy')
avg=0.0
for i in range(len(data)):
    avg+=data[i]
avg/=len(data)
print(avg)

avg=0.0
valid=66
for i in range(valid):
    avg+=data[i]
avg/=valid
print(avg)