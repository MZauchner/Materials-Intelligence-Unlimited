import serial


#mode = input('choose your operating mode:')
def slidesilo(mode,com_port="/dev/ttyACM0"):
    ser = serial.Serial(com_port, 9600)

    if mode == "rotate":
        
        ser.write(mode.encode("utf-8"))

    elif mode == "forward":
        ser.write(mode.encode("utf-8"))

    elif mode == "backward":
        ser.write(mode.encode("utf-8"))
