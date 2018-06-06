# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 10:52:25 2018

@author: tanac upper right USB
"""

import time

import serial


def rodsilo(D1, com_port="/dev/ttyACM0"):
    """1 moves rod into hold and 2 pushes rod out of holder"""
    #D1= "1"
    #change to "1" or "2" depending on the command you would want to execute manually.
    ser = serial.Serial(com_port, 9600)
    time.sleep(3)
    ser.write(D1.encode("utf-8"))
    time.sleep(3)
    print(ser.readline())
    time.sleep(3)
    ser.close()
