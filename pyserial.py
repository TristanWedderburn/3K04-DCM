# this is a tes for pyerial
import serial
import time
from struct import *
from binascii import *
#ser = serial.Serial('COM5',115200) # Change the comport and the Baudrate depending on specification

#print(ser.name)
#ser.isOpen()

#print("port open")

# dataSend = [0.0,55.0,6.0,22.5,8.3,300.5,8.2,22.5,446.3,11.1,5.99,0.73,9.4,3.1] # represents the data that will be sent to the DCM, this will be a a value 
# #strSend  = toString(dataSend)

# strFormat = "bbbdddddddddddddbbbbb" #SYNC, FN_CODE , PACE_MODE, LOWER_LIMIT, UPPER_LIMIT, MAX_SENS_RATE,A_AMPLITUDE, 
#V_AMPLITUDE, A_PULSEWIDTH, V_PULSEWIDTH, A_SENSITIVITY, VRP, ARP, PVARP, HYSTERESIS, RATESMOOTTHING,
#ACTIVITY_TRHESHOLD, REACTION_TIME, RESPONSE_FACTOR,RECOVERY_TIME
'''
packed = pack(strFormat,
    SYNC,
    FN_CODE,
    MODE,
    userDatabase[currentUser].parameters[mode][0],
    userDatabase[currentUser].parameters[mode][1],
    userDatabase[currentUser].parameters[mode][2],
    userDatabase[currentUser].parameters[mode][3],
    userDatabase[currentUser].parameters[mode][4],
    userDatabase[currentUser].parameters[mode][5],
    userDatabase[currentUser].parameters[mode][6],
    userDatabase[currentUser].parameters[mode][7],
    userDatabase[currentUser].parameters[mode][8],
    userDatabase[currentUser].parameters[mode][9],
    userDatabase[currentUser].parameters[mode][10],
    userDatabase[currentUser].parameters[mode][11],
    userDatabase[currentUser].parameters[mode][12],
    userDatabase[currentUser].parameters[mode][13],
    userDatabase[currentUser].parameters[mode][14],
    userDatabase[currentUser].parameters[mode][15],
    userDatabase[currentUser].parameters[mode][16],
    userDatabase[currentUser].parameters[mode][17])


'''

#packed = pack('dddddddddddddbbbbb',35.0, 175.0, 0.0, 0.0, 2.1, 0.0, 1.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 7, 0, 0, 0)
# packed = pack("d",13.0)
# print(packed)
# print(hexlify("*"))
# print(unpack("d",packed))
# what we need to put here. 
#ser.write(1001)
# figure out how to recive data
#ser.close()

#unpacked = unpack("b",packed)
#print(unpacked) 
# values = bytearray([4, 9, 62, 144, 56, 30, 147, 3, 210, 89, 111, 78, 184, 151, 17, 129])
# print(values)

byte_obj = bytes(b'\x16')
print('1')
print(byte_obj)
byte = chr(0x40)
print(byte)

print("%01#RDD0010000107**\r".encode())

start = int('35').to_bytes(8,byteorder = "big", signed = False)
print(start[:1])
print(start[1:2])
print(start[2:3])
print(start[3:4])
print(start[4:5])
print(start[5:6])
print(start[6:7])
print(start[7:8])
# print(start[:1])

print('hello'.encode('utf-8'))