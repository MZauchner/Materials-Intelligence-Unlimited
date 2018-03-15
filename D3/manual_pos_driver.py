import time

import serial

##open the serial port when script is first run, and then invoke the
##functions - this should reduce access and execution time to the arduino
##wait for serial port to initialise
time.sleep(3)

##Sample specific parameters
rod_strike = 7
rod_pos = 30
slide_strike = 10
slide_pos = 160

##General parameters
##Serial port  - currently set for windows
##These need to match the values in the arduino script!
com_port = "COM3"
baud_rate = 115200
repeats = 5
centre_val = 75 ##this is the servo's central position

def move(obj):
    ##Composes the command string
    ser = serial.Serial(com_port, baud_rate)
    if obj == "rod":
        ser.write((str(0) + " " +
                   str(rod_pos) + " " +
                   str(0)).encode("utf-8"))

    elif obj == "slide":
        ser.write((str(0) + " " +
               str(slide_pos) + " " +
               str(0)).encode("utf-8"))

    elif obj == "centre":
        ser.write((str(0) + " " +
               str(centre_val) + " " +
               str(0)).encode("utf-8"))

def test(obj):
    ser = serial.Serial(com_port, baud_rate)
    if obj == "rod":
        ser.write((str(rod_strike) + " " +
                   str(-1) + " " +
                   str(repeats)).encode("utf-8"))

    elif obj == "slide":
        ser.write((str(slide_strike) + " " +
               str(-1) + " " +
               str(repeats)).encode("utf-8"))
