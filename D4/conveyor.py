
import serial


def conveyor(mode, com_port = '/dev/ttyACM0'):
    ser = serial.Serial(com_port, 9600)

    #mode = input('choose your operating mode:')

    if str(mode) == "1":
	    ser.write(mode.encode("utf-8"))

    elif str(mode) == "2":
	    ser.write(mode.encode("utf-8"))
