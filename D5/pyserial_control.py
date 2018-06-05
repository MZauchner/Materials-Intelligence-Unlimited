import serial


#mode = input('choose your operating mode:')
def slidesilo(mode):
    ser = serial.Serial('/dev/ttyACM0', 9600)

    if mode == "rotate":
        
        ser.write(mode.encode("utf-8"))

    elif mode == "forward":
        ser.write(mode.encode("utf-8"))

    elif mode == "backward":
        ser.write(mode.encode("utf-8"))
