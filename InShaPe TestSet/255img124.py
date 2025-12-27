'''
import tifffile
# Load TIFF image
tif = tifffile.imread('cal-sp4-50nm_crop.tif')
max=np.max(tif)
'''

import numpy as np
from PIL import Image
import os

folder='ring'
name=os.listdir(folder)
for i in range(len(name)):
    path=os.path.join(folder, name[i])
    png = Image.open(path)
    if png.mode != 'L':
        png = png.convert('L')
    png=np.array(png)
    png = (png / 255.0) * 124
    png=png.astype(np.uint16)
    png=Image.fromarray(png)
    png.save(path)
    print(i)