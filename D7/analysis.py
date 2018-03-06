import math
import subprocess
import sys

import numpy as np
import scipy.optimize as optimization
from matplotlib import pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
from scipy.signal import find_peaks_cwt

import Python3SolenoidDriver as p3
import soundfile as sf

sys.path.append('/Users/mariozauchner/Dev/VibratINC/D3')

def func_rod(datax,A0,w0,tau0,A1,w1,tau1):
    return A0*np.exp(-0.5*((datax-w0)/tau0)**2)+ A1*np.exp(-0.5*((datax-w1)/tau1)**2)

def func_slide(datax,A=200, w0=3000, tau = 5.5):
    return A*np.exp(-0.5*((datax-w0)/tau)**2)

def ddata(datax, datay):
    step = datax[1]-datax[0]
    ddatay = []
    ddatay.append(0)
    for i in range(len(datay)-1):
        ddatay.append((datay[i+1]-datay[i])/step)
    return ddatay

def analyze(accepted_deviation, rod_freq, slide_freq, sample):
    #fs, data = wavfile.read('proto.wav')
    if sample == "slide":
        upper_freq = slide_freq + accepted_deviation/2
        lower_freq = slide_freq - accepted_deviation/2
    if sample == "rod":
        upper_freq = rod_freq + accepted_deviation/2
        lower_freq = rod_freq - accepted_deviation/2

    #subprocess.Popen('arecord -Dhw:1 -c 2 -f S16_LE -r 11015 proto.wav', shell=True)
    #p3.test(sample)
    #subprocess.Popen("pkill arecord", shell=True)
    data, fs= sf.read('proto.wav')
    dt = 1/fs
    n= data.shape[0]
    k = numpy.arange(n)
    time = n/fs
    frequency = k/time
    frequency = frequency[range(int(int(n)/2))]
    print("time is "+ str(time))

    a = data.T[0]
    c = fft(a)
    c = c[range(int(int(n)/2))]
    d = len(c)/2
    plt.plot(frequency,abs(c),"r")
    plt.show()
    return frequency, abs(c)
