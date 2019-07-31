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

serCon = serial.Serial(None)
serCon.port = 'COM2'


serCon.open()

print(serCon.is_open)
                                 
for i in range(500):
    serCon.write(modeOne.generateLine())
    time.sleep(.2)
    
                                
                                 

                    