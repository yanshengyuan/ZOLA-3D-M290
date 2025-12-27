import numpy as np
import json as js
from os import listdir

gt=np.load('run0004_zernikeCoeff.npy')
filenames=listdir('./')
jsonlist=[]
for i in range(0,len(filenames)):
    index = filenames[i].split(".")[-1]
    if index=='json':
        jsonlist.append(filenames[i])
Mae=[]
for i in range(len(jsonlist)):
    Mae.append([])
for i in range(len(jsonlist)):
    mae=0.0
    Mae[i].append(jsonlist[i])
    with open(jsonlist[i],'r',encoding='utf8')as fp:
        json_data = js.load(fp)
        zernike=json_data['zernike']
        for j in range(3, len(zernike)):
            mae+=abs(zernike[j]-gt[j])

    mae/=12
    Mae[i].append(mae)