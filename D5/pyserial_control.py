import serial 

ser = serial.Serial('COM3', 9600)

mode = input('choose your operating mode:')

if mode == "rotate":
	ser.write(b'rotate')

elif mode == "forward":
	ser.write(b'forward')

elif mode == "backward":
	ser.write(b'backward')
