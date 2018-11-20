# this is a tes for pyerial
import serial
ser = serial.Serial('/dev/ttyUSB0') # change this later when we figure out
# what we need to put here. 
ser.write("fuck this class")
# figure out how to recive data
ser.close()

