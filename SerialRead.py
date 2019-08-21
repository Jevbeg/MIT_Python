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



for i in range(5) :
    a = (serCon.read_until(terminator = b'\r').decode("UTF-8"))
    print(a)
    
    
    #serCon.flushInput()
    #for counter in serCon.read_until(b'0') :
     
        

    
    
    
serCon.close()
print('done')











"""
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

"""
    

