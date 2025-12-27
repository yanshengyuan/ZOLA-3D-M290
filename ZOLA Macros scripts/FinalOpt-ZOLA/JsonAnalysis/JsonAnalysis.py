import numpy as np
import json as js
from os import listdir
import re

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

path='./json_bench/'
filenames=listdir('./json_bench/')
filenames=sorted_alphanumeric(filenames)
jsonlist=[]
for i in range(0,len(filenames)):
    index = filenames[i].split(".")[-1]
    if index=='json':
        jsonlist.append(path+filenames[i])

beamshape=[]
for i in range(len(jsonlist)):
    with open(jsonlist[i],'r',encoding='utf8')as fp:
        json_data = js.load(fp)
        zernike=json_data['zernike']
        zernike=zernike[3:]
        beamshape.append(zernike)

beamshape=np.array(beamshape)
np.save('bench.npy', beamshape)

path='./json_gaussian/'
filenames=listdir('./json_gaussian/')
filenames=sorted_alphanumeric(filenames)
jsonlist=[]
for i in range(0,len(filenames)):
    index = filenames[i].split(".")[-1]
    if index=='json':
        jsonlist.append(path+filenames[i])

beamshape=[]
for i in range(len(jsonlist)):
    with open(jsonlist[i],'r',encoding='utf8')as fp:
        json_data = js.load(fp)
        zernike=json_data['zernike']
        zernike=zernike[3:]
        beamshape.append(zernike)

beamshape=np.array(beamshape)
np.save('gaussian.npy', beamshape)

path='./json_tear/'
filenames=listdir('./json_tear/')
filenames=sorted_alphanumeric(filenames)
jsonlist=[]
for i in range(0,len(filenames)):
    index = filenames[i].split(".")[-1]
    if index=='json':
        jsonlist.append(path+filenames[i])

beamshape=[]
for i in range(len(jsonlist)):
    with open(jsonlist[i],'r',encoding='utf8')as fp:
        json_data = js.load(fp)
        zernike=json_data['zernike']
        zernike=zernike[3:]
        beamshape.append(zernike)

beamshape=np.array(beamshape)
np.save('tear.npy', beamshape)

path='./json_rec/'
filenames=listdir('./json_rec/')
filenames=sorted_alphanumeric(filenames)
jsonlist=[]
for i in range(0,len(filenames)):
    index = filenames[i].split(".")[-1]
    if index=='json':
        jsonlist.append(path+filenames[i])

beamshape=[]
for i in range(len(jsonlist)):
    with open(jsonlist[i],'r',encoding='utf8')as fp:
        json_data = js.load(fp)
        zernike=json_data['zernike']
        zernike=zernike[3:]
        beamshape.append(zernike)

beamshape=np.array(beamshape)
np.save('rec.npy', beamshape)

path='./json_hat/'
filenames=listdir('./json_hat/')
filenames=sorted_alphanumeric(filenames)
jsonlist=[]
for i in range(0,len(filenames)):
    index = filenames[i].split(".")[-1]
    if index=='json':
        jsonlist.append(path+filenames[i])

beamshape=[]
for i in range(len(jsonlist)):
    with open(jsonlist[i],'r',encoding='utf8')as fp:
        json_data = js.load(fp)
        zernike=json_data['zernike']
        zernike=zernike[3:]
        beamshape.append(zernike)

beamshape=np.array(beamshape)
np.save('hat.npy', beamshape)

path='./json_ring/'
filenames=listdir('./json_ring/')
filenames=sorted_alphanumeric(filenames)
jsonlist=[]
for i in range(0,len(filenames)):
    index = filenames[i].split(".")[-1]
    if index=='json':
        jsonlist.append(path+filenames[i])

beamshape=[]
for i in range(len(jsonlist)):
    with open(jsonlist[i],'r',encoding='utf8')as fp:
        json_data = js.load(fp)
        zernike=json_data['zernike']
        zernike=zernike[3:]
        beamshape.append(zernike)

beamshape=np.array(beamshape)
np.save('ring.npy', beamshape)