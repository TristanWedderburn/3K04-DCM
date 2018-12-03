import time
import serial
import struct

array=[22, 1, 2, 35.0, 175.0, 0.0, 0.0, 2.1, 0.0, 1.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0]
print(array)
print(struct.pack('iiidddddddddddddiiiii',*array))