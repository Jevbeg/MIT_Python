# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 23:38:21 2019

@author: Alien
"""

import serial
import time
import matplotlib.pyplot as plt


serCon = serial.Serial(None)

serCon.port = 'COM4'

indic = 1

serCon.baudrate = 19200
serCon.timeout = None

filename = time.strftime("%Y%m%d_%H%M", time.localtime())
logFile = open("{}.txt".format(filename), "w")

print(serCon.is_open)


if not serCon.is_open :
    serCon.open()


try :
    while True :
        receivedLine = (serCon.read_until(terminator = b'\r').decode("UTF-8"))
        print(receivedLine)
        print(receivedLine[1 : (len(receivedLine)-1)])
        print(receivedLine.split("\t"))
        print(receivedLine[1 : (len(receivedLine)-1)].split("\t"))
        logFile.writelines(receivedLine)

except KeyboardInterrupt :
    serCon.close()
    logFile.close()
    pass
        
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
    

