# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 00:07:33 2019

@author: Alien
"""

import serial
import time

ser = serial.Serial(None)
#ser.write(b'sdgdfhfghfgj')
ser.port = 'COM2'
print(ser.name)
ser.open()
print(ser.is_open)
"""ser.open()"""
ser.write(b'once again')
ser.write(b'\n')

txtInASCII = ''

for i in range(10):
       
    txtInASCII = str(i) + '\r' + '\n'

    time.sleep(1)
    ser.write(txtInASCII.encode("ASCII", "ignore"))

ser.close()

print(ser.is_open)

"""
print(ser.name)
ser.write('well, hi there')
ser.close()
"""
