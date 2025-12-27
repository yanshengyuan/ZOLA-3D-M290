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

filename="hat"

def RMSE(wave1, wave2):
    mse=0.0
    for x in range(len(wave1)):
        for y in range(len(wave1[x])):
            mse += (wave1[x][y]-wave2[x][y])**2
    mse=mse/((len(wave1))**2)
    rmse=math.sqrt(mse)
    return rmse

# Define paths and filenames for input
inputPathStr="./Input_Data/"
configFileStr="Config_AI_Data_Generator.dat"

# Open data generator config file
config = configparser.ConfigParser()
checkFile = config.read(inputPathStr+configFileStr)

# Define initial field
wavelength = config["field_initialization"].getfloat("wavelength")
gridSize = config["field_initialization"].getfloat("gridSize")
gridPixelnumber = config["field_initialization"].getint("gridPixelnumber")
beamDiameter = config["gaussian_beam"].getfloat("beamDiameter")
beamWaist = beamDiameter/2

lightField = Begin(gridSize,wavelength,gridPixelnumber)
lightField = GaussBeam(lightField, beamWaist, n = 0, m = 0, x_shift = 0, y_shift=0, tx=0, ty=0, doughnut=False, LG=True)
gaussian_mask = Intensity(lightField)
mask_avg = np.mean(gaussian_mask)
gaussian_mask=gaussian_mask/mask_avg

# Prepare and apply CGH phase mask to field
cghFilename = config["cgh_data"]["cghFilename"]
cghBackgroundValue = config["cgh_data"].getint("cghBackgroundValue") 
cghGreyValues = config["cgh_data"].getint("cghGreyValues")
cghSize = config["cgh_data"].getfloat("cghSize")
cghPixelNumber = config["cgh_data"].getint("cghPixelNumber")

cghImageData = mpimg.imread(inputPathStr + cghFilename) 
cghPhaseData = 2*np.pi*(np.asarray(cghImageData[:,100:700])-cghBackgroundValue/cghGreyValues)

cghField=Begin(cghSize,wavelength,cghPixelNumber)
cghField=MultPhase(cghField,cghPhaseData)
cghField=Interpol(cghField, gridSize, gridPixelnumber, x_shift=0.0, y_shift=0.0, angle=0.0, magnif=1.0)

lightField=MultPhase(lightField,Phase(cghField))
masked_CGHapplied=Phase(lightField)*gaussian_mask
#mpimg.imsave(phaseimg_path+"2-Masked-CGH_PhaseMask_applied.png",masked_CGHapplied,cmap='Greys')

# Prepare calculation of Zernike coefficients      
zernikeMaxOrder = config["zernike_coefficients"].getint("zernikeMaxOrder")
zernikeAmplitude = config["zernike_coefficients"].getfloat("zernikeAmplitude")
zernikeRadius = config["zernike_coefficients"].getfloat("zernikeRadius")
nollMin = config["zernike_coefficients"].getint("nollMin")


nollMax = np.sum(range(1,zernikeMaxOrder + 1))  # Maximum Noll index
nollRange=range(nollMin,nollMax+1)
zernikeCoeff=np.zeros(nollMax)

# Prepare main control loop
runMax = config["run_control"].getint("runMax")

#Prepare field focusing 
beamMagnification = config["field_focussing"].getfloat("beamMagnification")
focalLength = config["field_focussing"].getfloat("focalLength") / beamMagnification
focalReduction = config["field_focussing"].getfloat("focalReduction")
                   
f1=focalLength*focalReduction
f2=f1*focalLength/(f1-focalLength)
frac=focalLength/f1
newSize=frac*gridSize
newExtent=[-newSize/2/mm,newSize/2/mm,-newSize/2/mm,newSize/2/mm]

#Prepare field aperture
apertureRadius = config["field_aperture"].getfloat("apertureRadius")
apertureSmoothWidth = config["field_aperture"].getfloat("apertureSmoothWidth")

# Prepare propagation of field to caustic planes
focWaist = wavelength/np.pi*focalLength/beamWaist  # Focal Gaussian beam waist
zR = np.pi*focWaist**2/wavelength # Rayleigh range focused Gaussian beam

causticPlanes = []
causticPlanes.append(("-01-pre-", config["caustic_planes"].getfloat("prefocPlane") ))
causticPlanes.append(("-02-foc-", config["caustic_planes"].getfloat("focPlane")) )
causticPlanes.append(("-03-pst-", config["caustic_planes"].getfloat("postfocPlane") )) 

# Prepare intensity output
outputSize = config["data_output"].getfloat("outputSize")
outputPixelnumber = config["data_output"].getint("outputPixelnumber")

pred=np.load(filename+".npy")
gt=np.load("gt.npy")
Metrics=[]
# Initialize and start main control loop
for runCount in range(0,runMax):
    print(runCount)
    
    # Generate and apply Zernike phase distortion      
    distField = lightField
    zernikeField = lightField
    distField_pred = lightField
    zernikeField_pred = lightField
    
    zernikecoefficients = pred[runCount]
    zGT = gt[runCount]

    mae = 0.0
    for x in range(len(zGT)):
        mae += abs(zernikecoefficients[x]-zGT[x])
    mae = mae/len(zGT)
    
    #Apply aberrations
    for countNoll in nollRange: 
        if countNoll>3:
            (nz,mz) = noll_to_zern(countNoll)
            zernikeCoeff[countNoll-1] = zGT[countNoll-4]
            zernikeField = Zernike(zernikeField,nz,mz,zernikeRadius,zernikeCoeff[countNoll-1],units='rad')
        else:
            (nz,mz) = noll_to_zern(countNoll)
            zernikeCoeff[countNoll-1] = 0
            zernikeField = Zernike(zernikeField,nz,mz,zernikeRadius,zernikeCoeff[countNoll-1],units='rad')
    distField = zernikeField
    aberrated_wavefront = Phase(distField)
    masked_aberrated_wavefront=aberrated_wavefront*gaussian_mask
    #mpimg.imsave(phaseimg_path+str(runCount)+"-"+"3-masked-zernike_aberrations_added.png",masked_aberrated_wavefront,cmap='Greys')
    # Prefocus field and apply aperture
    distField = Lens(f1,0,0,distField)
    distField = SmoothCircAperture(distField, apertureRadius, apertureSmoothWidth)
    # Reconstruction Error computed here
    GTintensity=[]
    for causticStr,causticPos in causticPlanes:
        cField=LensFresnel(distField,f2,focalLength+causticPos*zR)
        cField=Convert(cField)
        outputField=Interpol(cField,outputSize,outputPixelnumber)
        intensity_gt=Intensity(outputField)
        GTintensity.append(intensity_gt)

    #Correct aberrations
    for countNoll in nollRange: 
        if countNoll>3:
            (nz,mz) = noll_to_zern(countNoll)
            zernikeCoeff[countNoll-1] = -zernikecoefficients[countNoll-4]
            zernikeField = Zernike(zernikeField,nz,mz,zernikeRadius,zernikeCoeff[countNoll-1],units='rad')
        else:
            (nz,mz) = noll_to_zern(countNoll)
            zernikeCoeff[countNoll-1] = 0
            zernikeField = Zernike(zernikeField,nz,mz,zernikeRadius,zernikeCoeff[countNoll-1],units='rad')
    distField = zernikeField
    corrected_wavefront = Phase(distField)
    masked_corrected_wavefront=corrected_wavefront*gaussian_mask
    wavefront_error=RMSE(masked_CGHapplied, masked_corrected_wavefront)
    #mpimg.imsave(phaseimg_path+str(runCount)+"-"+"4-masked-after_NeuralNetwork's_Correction.png",masked_corrected_wavefront,cmap='Greys')      
    
    #Reconstruction Error computed here
    for countNoll in nollRange: 
        if countNoll>3:
            (nz,mz) = noll_to_zern(countNoll)
            zernikeCoeff[countNoll-1] = zernikecoefficients[countNoll-4]
            zernikeField_pred = Zernike(zernikeField_pred, nz, mz, zernikeRadius, zernikeCoeff[countNoll-1], units='rad')
        else:
            (nz,mz) = noll_to_zern(countNoll)
            zernikeCoeff[countNoll-1] = 0
            zernikeField_pred = Zernike(zernikeField_pred, nz, mz, zernikeRadius, zernikeCoeff[countNoll-1], units='rad')
    distField_pred = zernikeField_pred
    # Prefocus field and apply aperture
    distField_pred = Lens(f1,0,0,distField_pred)
    distField_pred = SmoothCircAperture(distField_pred, apertureRadius, apertureSmoothWidth)
    # Reconstruction Error computed here
    PRDintensity=[]
    for causticStr,causticPos in causticPlanes:
        cField_pred=LensFresnel(distField_pred,f2,focalLength+causticPos*zR)
        cField_pred=Convert(cField_pred)
        outputField_pred=Interpol(cField_pred,outputSize,outputPixelnumber)
        intensity_pred=Intensity(outputField_pred)
        PRDintensity.append(intensity_pred)
    rmse=[]
    for i in range(len(GTintensity)):
        rmse.append(RMSE(GTintensity[i], PRDintensity[i]))
    reconstruction_error=0.0
    for i in range(len(rmse)):
        reconstruction_error+=rmse[i]
    reconstruction_error=reconstruction_error/len(rmse)
    
    Metrics.append([wavefront_error, mae, reconstruction_error, runCount])

AvgWavefrontErr=0.0
for i in range(len(Metrics)):
    AvgWavefrontErr+=Metrics[i][0]
AvgWavefrontErr=AvgWavefrontErr/len(Metrics)

AvgMAE=0.0
for i in range(len(Metrics)):
    AvgMAE+=Metrics[i][1]
AvgMAE=AvgMAE/len(Metrics)

AvgReconsErr=0.0
for i in range(len(Metrics)):
    AvgReconsErr+=Metrics[i][2]
AvgReconsErr=AvgReconsErr/len(Metrics)

print("WaveFront Error(phase):%f"%(AvgWavefrontErr))
print("MAE(zernike coefficients):%f"%(AvgMAE))
print("Reconstruction Error(intensity):%f"%(AvgReconsErr))

Metrics.sort(key=lambda x:x[2])
Metrics_np = np.array(Metrics)
np.save(filename+"_Metrics.npy",Metrics_np)

Metrics_pd=pd.DataFrame(Metrics_np[:,:3], columns=['WavefrontErr','MAE','ReconsErr'])
pd.plotting.scatter_matrix(Metrics_pd, alpha=0.15, figsize=None, ax=None, grid=False,
                           diagonal='hist', marker='.', density_kwds=None, hist_kwds=None,
                           range_padding=0.0)
plt.savefig(filename+"Scatter_Matrix.png",dpi=1000, bbox_inches='tight')