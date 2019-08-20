# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 00:07:33 2019

@author: Alien
"""
import serial
import time
import random



"""MAIN BODY STARTS HERE""" 

#We initiate Serial class instances as empty (in case they weren't closed)
serCon1 = serial.Serial(None)
serCon3 = serial.Serial(None)

serCon1.port = 'COM1'
serCon3.port = 'COM3'

serCon1.open()
serCon3.open()

fl = open("example.txt", "r")

line = ""

for i in range(10):

    line = fl.readline()
    print(line)
    print(str(len(line)))
    if ('#1' in line) or ('#2' in line):
        line = line[0:(len(line)-1)]
        
        serCon1.write(line.encode('ascii'))
        serCon1.write(b'\r')
        time.sleep(1)
    else :
        serCon1.write(line.encode('ascii'))
        serCon1.write(b'\r')
    
    
    


fl.close()

serCon1.write(b'once again')
serCon1.write(b'\n')

txtInASCII = ''


serCon1.close()
serCon3.close()








""" ---------------Code chunks-------------------------
print(serCon1.name)
serCon1.write('well, hi there')
serCon1.close()

for i in range(10):
       
    txtInASCII = str(i) + '\r' + '\n'

    time.sleep(1)
    serCon1.write(txtInASCII.encode("ASCII", "ignore"))



"""
