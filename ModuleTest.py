# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 23:43:29 2019

@author: Alien
"""

import hygen_module
import time 
import serial 

modeOne = hygen_module.stateLine('#1')
modeTwo = hygen_module.stateLine('#2')

serCon1 = serial.Serial(None)
serCon1.port = 'COM1'
serCon3 = serial.Serial(None)
serCon3.port = 'COM3'

serCon1.open()
serCon3.open()



print(serCon1.is_open)
print(serCon3.is_open)

for i in range(50):
    
    gLine = modeOne.generateLine()
    
    serCon1.write(gLine)
    serCon3.write(gLine)
    
    time.sleep(.2)

modeTwo.continueFrom(modeOne)

for i in range(50):
    gLine = modeTwo.generateLine()
    serCon1.write(gLine)
    time.sleep(.2)
    
serCon1.close()
serCon3.close() 
                                
                                 

                    