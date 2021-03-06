import serial
import time

def hammer_time(com, baud, impact_time, head_pos, delay, reps):
    ser = serial.Serial(com_port, baud_rate)
    ##wait for serial port to initialise
    time.sleep(3)
    ##Composes the command string
    ser.write((str(impact_time) + " " +  
               str(head_pos) + " " +
               str(delay) + " " +
               str(reps)).encode("utf-8"))
    ##waits for the arduino to finish recieving information
    time.sleep(3)
    ##debug statement for checking what command was sent
    print(ser.readline())
    ser.close()

##Serial port  - currently set for windows
##These need to match the values in the arduino script!
com_port = "COM4"
baud_rate = 115200

##Pause between servo movement and testing
##use 500 for testing and 2000 for actual operation
delay = 2000
repeats = 5
##first number is in minutes - converted to ms
hold_time = 5 *60*1000

##Sample specific parameters
rod_strike = 7
rod_pos = 30
slide_strike = 10
slide_pos = 130

def test(command):
    if command == "rod test":
        ##Tests the rod
        hammer_time(com_port, baud_rate, rod_strike, rod_pos, delay, repeats)
    elif command == "slide test":
        ##tests the slide
        hammer_time(com_port, baud_rate, slide_strike, slide_pos, delay, repeats)
    elif command == "rod hold":
        ##holds the test head above the rod for the hold time
        hammer_time(com_port, baud_rate, 0, rod_pos, hold_time, 0)
    elif command == "slide hold":
        ##holds the test head above the slide for the hold time
        hammer_time(com_port, baud_rate, 0, slide_pos, hold_time, 0)
