import numpy as np

data=np.load('tear_Metrics.npy')
avg=0.0
for i in range(len(data)):
    avg+=data[i][0]
avg/=len(data)
print(avg)

avg=0.0
valid=92
for i in range(valid):
    avg+=data[i][0]
avg/=valid
print(avg)