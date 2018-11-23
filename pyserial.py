# this is a tes for pyerial
import serial
import time
from struct import *
#ser = serial.Serial('COM5',115200) # Change the comport and the Baudrate depending on specification

#print(ser.name)
#ser.isOpen()

#print("port open")

dataSend = [0.0,55.0,6.0,22.5,8.3,300.5,8.2,22.5,446.3,11.1,5.99,0.73,9.4,3.1] # represents the data that will be sent to the DCM, this will be a a value 
#strSend  = toString(dataSend)

strFormat = "bbbdddddddddddddbbbbb" #SYNC, FN_CODE , PACE_MODE, LOWER_LIMIT, UPPER_LIMIT, MAX_SENS_RATE,A_AMPLITUDE, 
#V_AMPLITUDE, A_PULSEWIDTH, V_PULSEWIDTH, A_SENSITIVITY, VRP, ARP, PVARP, HYSTERESIS, RATESMOOTTHING,
#ACTIVITY_TRHESHOLD, REACTION_TIME, RESPONSE_FACTOR,RECOVERY_TIME
packed = pack(strFormat,
    SYNC,
    FN_CODE,
    MODE,
    






)
print(packed)
# what we need to put here. 
#ser.write(1001)
# figure out how to recive data
#ser.close()

unpacked = unpack("b",packed)
print(unpacked)