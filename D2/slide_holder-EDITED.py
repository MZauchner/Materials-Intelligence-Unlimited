# D2 Slide Holder group
# This code is to control the Arduino code d2-slideholder.ino 

#   Import the serial library
import serial

#Establish connection to Arduino via serial port
arduinoData = serial.Serial('COM8',9600)

# Create variable motion to determine how the slide holder's part should rotate
motion = input('Which direction do you want to move in?:')

# Assign numerals to send to Arduino for a given string
if motion == "cw":
    arduinoData.write(1)
    
elif motion == "ccw":
    arduinoData.write(2)
    
elif motion == "both":
    arduinoData.write(3)
