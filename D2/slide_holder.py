import serial

arduinoData = serial.Serial('COM8',9600)

def clockwise():
    arduinoData.write(1)

def counterclockwise():
    arduinoData.write(2)
    
def both():
    arduinoData.write(3)
    
both()