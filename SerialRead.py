# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 23:38:21 2019

@author: Alien
"""

import serial
#import time

serCon = serial.Serial(None)

serCon.port = 'COM2'

indic = 1

serCon.baudrate = 19200
serCon.timeout = None
print(serCon.is_open)
if not serCon.is_open : 
    serCon.open()

data = []
dataline = ''
quit_command = 0

while True :
    print(indic)
    indic += 1
    for counter in serCon.read_until(b'0') :
        data.append(counter)
    dataline = str(bytes(data))
    data.clear()
    serCon.reset_input_buffer()
    print(dataline)
    #quit_command = int(serCon.read(1))
    print(indic)
    indic += 1
    serCon.write(b'Are you still there?')
    print(indic)
    indic += 1
serCon.close()
print('done')
    

