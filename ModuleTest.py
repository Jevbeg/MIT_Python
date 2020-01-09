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

# serCon3 = serial.Serial(None)
# serCon3.port = 'COM3'

serCon1.open()
# serCon3.open()

serCon1.baudrate = 19200
# serCon3.baudrate = 19200

print(serCon1.is_open)
# print(serCon3.is_open)

while True:
    try: 
        for i in range(500):
            
            gLine = modeOne.generateLine()
            
            serCon1.write(gLine)
            # serCon3.write(gLine)
            
            time.sleep(1)
        
#        modeTwo.continueFrom(modeOne)
        
#        for i in range(100):
#            gLine = modeTwo.generateLine()
#            serCon1.write(gLine)
#            time.sleep(0.5)
        
    except KeyboardInterrupt:
        print('Manually interrupted')
        serCon1.close()
        # serCon3.close() 
        

                                
                                 

                    