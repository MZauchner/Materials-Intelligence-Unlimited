# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 10:52:25 2018

@author: tanac
"""

import serial 
import time 

D1= "1"
ser = serial.Serial("COM6",9600)
time.sleep(3)

ser.write(D1.encode("utf-8"))
time.sleep(3)
print(ser.readline())
time.sleep(3)

ser.close()