from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft
import numpy
import math
from scipy.signal import find_peaks_cwt
import scipy.optimize as optimization
import numpy as np
import sys
import subprocess

sys.path.append('/home/pi/bin/VibratINC/D3')

import soundfile as sf
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

    subprocess.Popen('arecord -Dhw:1 -c 2 -f S16_LE -r 11015 proto.wav', shell=True)    
    import hammer_time
    subprocess.Popen("pkill arecord", shell=True)
    data, fs= sf.read('proto.wav')
    #data = data/ (2.**15)
    #data = data[23000:]
    dt = 1/fs
    n= data.shape[0]
    #print(n)
    k = numpy.arange(n)
    time = n/fs
    frequency = k/time
    frequency = frequency[range(int(int(n)/2))]
    #frequency = frequency[1000:]
    print("time is "+ str(time))

    a = data.T[0]
    c = fft(a)
    c = c[range(int(int(n)/2))]
    d = len(c)/2
    #c = c[1000:]
    #sigma= peak_finder.peak_finder(c)
    #c[c<0.01*max(abs(c))]=0
    #c[c<max(c)]=0
    #dd = ddata(frequency, abs(c))
    #fit = optimization.curve_fit(func_rod, frequency, abs(c), bounds = [[0,3000,1,0,3300,1],[max(abs(c)),3500,10,max(abs(c)),3500,10]])
    #:wq
    #plt.plot(a[1000:])
    #plt.plot(a)
    #plt.plot(sigma)
    #print(fit)
    #peaks = peakutils.indexes(c, thres=0.6, min_dist=10)
    #peaks = peaks[frequency[peaks]>900]
    #print([frequency[peak] for peak in peaks])
    plt.plot(frequency,abs(c),"r")
    #for i in range(len(sigma)):
    #    if sigma[i]<=0.04:
    #        plt.axvline(frequency[i])
    #plt.plot(frequency,sigma)
    #plt.plot(frequency, dd)
    #plt.plot(frequency, func_rod(frequency, fit[0][0], fit[0][1],fit[0][2], fit[0][3],fit[0][4],fit[0][5]))
    #plt.imshow(M)
    #plt.colorbar()
    plt.show()
