import math
import subprocess
import sys
import time

import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft
#sys.path.append('/home/pi/bin/VibratINC/D3/')
sys.path.append('/Users/mariozauchner/Dev/VibratINC/D3')
import manual_pos_driver as p3
import soundfile as sf


"""
def func_rod(datax,A0,w0,tau0,A1,w1,tau1):
    return A0*np.exp(-0.5*((datax-w0)/tau0)**2)+ \
    A1*np.exp(-0.5*((datax-w1)/tau1)**2)

def func_slide(datax,A=200, w0=3000, tau = 5.5):
    return A*np.exp(-0.5*((datax-w0)/tau)**2)

def ddata(datax, datay):
    step = datax[1]-datax[0]
    ddatay = []
    ddatay.append(0)
    for i in range(len(datay)-1):
        ddatay.append((datay[i+1]-datay[i])/step)
    return ddatay
"""
def analyze(sample, mode="test"):


    if mode == "recording":

        """record for 10 seconds"""

        subprocess.Popen('arecord -Dhw:1 -c 2 -f S16_LE -r 11015 proto.wav', \
        shell=True)#launch recording in shell
        time.sleep(10) #wait for 10 seconds
        subprocess.Popen("pkill arecord", shell=True)#kill shell process
    else:

        """launch subprocess for recording and excitation of sample"""

        subprocess.Popen('arecord -Dhw:1 -c 2 -f S16_LE -r 11015 proto.wav', \
        shell=True)#launch recording in shell
        p3.move(sample)
        p3.test(sample)#call excitation function of excitation group
        time.sleep(2)
        subprocess.Popen("pkill arecord", shell=True)#kill shell process

    data, fs= sf.read('proto.wav') # loading waveform

    """scaling of x-axis data to get correct frequencies"""

    dt = 1/fs #calculate frequency resolution
    n= data.shape[0] #get number of fft points
    k = np.arange(n) #create 1D-array sequence with length of number
    #of fft point (0, 1,2,3...)
    time = n/fs #get total time measured
    frequency = k/time #scale 1-D array to get correct frequencies
    frequency = frequency[range(int(int(n)/2))] #removal of redundant
    #points (symmetry of FFT)
    print("time is "+ str(time))

    a = data.T[0] #get waveform data from channel 1
    #print(a)
    c = fft(a) #fourier transform
    c = c[range(int(int(n)/2))] #removal of redundant points (symmetry of FFT)
    return frequency, abs(c)
