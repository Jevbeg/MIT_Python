# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 23:38:21 2019

@author: Alien
"""

import serial
#import time

ser2 = serial.Serial(None)

ser2.port = 'COM2'

ser2.baudrate = 19200
ser2.timeout = None


print(ser2.is_open)
if not ser2.is_open : 
    ser2.open()

data = []
dataline = ''
quit_command = 0

while True :
    print('line1')
    for counter in ser2.read_until(b'0') :
        data.append(counter)
    dataline = str(bytes(data))
    data.clear()
    ser2.reset_input_buffer()
    print(dataline)
    #quit_command = int(ser2.read(1))
    print('line2')
    ser2.write(b'Are you still there?')
    print('line3')
ser2.close()
print('done')
    

