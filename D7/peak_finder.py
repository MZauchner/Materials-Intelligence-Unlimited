import numpy as np
from matplotlib import pyplot as plt
import math
import random

def peak_finder(data):
    data = abs(data)
    N = len(data)
    L = N/2
    L = math.ceil(L)-1
    M = np.zeros((L,N))
    for k in range(L):
        k = k
        for i in range(k+2, N-k):
            if data[i-1]>data[i-k-1] and data[i-1]> data[i+k-1]:
                M[k,i]=0
            else:
                M[k,i]= random.uniform(0,1)+1

        for i in range(0,k):
            M[k,i]= random.uniform(0,1)+1
        for i in range(N-k+1, N):
             M[k,i]= random.uniform(0,1)+1

    gamma = np.sum(M, axis = 1)
    lamd = np.argmin(gamma)
    M_r = M[range(lamd),:]
    sigma = []
    sum_M_r = np.sum(M_r, axis=0)
    for i in range(N):
         sigma_i = 0
         for k in range(lamd):
               sigma_i += (1/(lamd-1))*abs(M_r[k,i]-sum_M_r[i]/lamd)
         sigma.append(sigma_i)
    return sigma
