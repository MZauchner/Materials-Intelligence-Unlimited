import serial
import time

##General parameters
##Serial port  - currently set for windows
##These need to match the values in the arduino script!
com_port = "COM5"
baud_rate = 115200
repeats = 5
centre_val = 75 ##this is the servo's central position

##Sample specific parameters
rod_strike = 7
rod_pos = 137
slide_strike = 10
slide_pos = 10

##open the serial port when script is first run, and then invoke the 
##functions - this should reduce access and execution time to the arduino
ser = serial.Serial(com_port, baud_rate)
##wait for serial port to initialise
time.sleep(3)

def move(obj):
    ##Moves test head to rod position
    if obj == "rod":
        ser.write((str(0) + " " +  
                   str(rod_pos) + " " +
                   str(0)).encode("utf-8"))
    
    ##moves test head to the slide position
    elif obj == "slide":
        ser.write((str(0) + " " +  
               str(slide_pos) + " " +
               str(0)).encode("utf-8"))
    
    ##moves test head to the central position
    elif obj == "centre":
        ser.write((str(0) + " " +  
               str(centre_val) + " " +
               str(0)).encode("utf-8"))
        
def test(obj):
    ##actuates the solenoid at current position with the rod parameters
    if obj == "rod":
        ser.write((str(rod_strike) + " " +  
                   str(-1) + " " +
                   str(repeats)).encode("utf-8"))
        
    ##actuates the solenoid at current position with the slide parameters
    elif obj == "slide":
        ser.write((str(slide_strike) + " " +  
               str(-1) + " " +
               str(repeats)).encode("utf-8"))
        
        