import numpy as np

data=np.load('gaussian_Metrics.npy')
avg=0.0
for i in range(len(data)):
    avg+=data[i][0]
avg/=len(data)
print(avg)

avg=0.0
valid=100
for i in range(valid):
    avg+=data[i][0]
avg/=valid
print(avg)