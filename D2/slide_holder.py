# D2 Slide Holder group
# This code is to control the Arduino code d2-slideholder.ino
#upper left usb port
#   Import the serial library
import serial


#Establish connection to Arduino via serial port
def slideholder(motion):
    arduinoData = serial.Serial('/dev/ttyACM2',9600)

    # Create variable motion to determine how the slide holder's part should rotate
    #motion = input('Which direction do you want to move in?:')

    # Assign numerals to send to Arduino for a given string
    if motion == "cw":
        arduinoData.write('1'.encode("utf-8")) # Send over data as bytes to Arduino

    elif motion == "ccw":
        arduinoData.write('2'.encode("utf-8"))

    elif motion == "both":
        arduinoData.write('3'.encode("utf-8"))

    arduinoData.close()
