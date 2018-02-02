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
com_port = "COM5"
baud_rate = 115200

##Pause between servo movement and testing
##use 500 for testing and 2000 for actual operation
delay = 2000
repeats = 5

hammer_time(com_port, baud_rate, 7, 180, delay, repeats)

###intercalated power and impact time test - will be used for force calibration
#for power in range(800, 1030, 10):
#    for impact_time in range(1,21):
#        hammer_time(com_port, baud_rate, impact_time, 120, delay, power)
#        print("Power level:" + str(power))
#        print("Switch-on Time:" + str(impact_time))