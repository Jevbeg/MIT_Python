# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 00:07:33 2019

@author: Alien
"""
import serial
import time

#class stateLine:
    

#def genLine()
    


"""MAIN BODY STARTS HERE""" 


serCon = serial.Serial(None)
#serCon.write(b'sdgdfhfghfgj')
serCon.port = 'COM2'
print(serCon.name)
serCon.open()
print(serCon.is_open)
"""serCon.open()""" 

fl = open("example.txt", "r")

line = ""

for i in range(30):

    line = fl.readline()
    print(line)
    print(str(len(line)))
    if ('#1' in line) or ('#2' in line):
        line = line[0:(len(line)-1)]
        
        serCon.write(line.encode('ascii'))
        serCon.write(b'\r')
        time.sleep(1)
    else :
        serCon.write(line.encode('ascii'))
        serCon.write(b'\r')
    
    
    


fl.close()

serCon.write(b'once again')
serCon.write(b'\n')

txtInASCII = ''


print(serCon.is_open)

serCon.close()

""" ---------------Code chunks-------------------------
print(serCon.name)
serCon.write('well, hi there')
serCon.close()

for i in range(10):
       
    txtInASCII = str(i) + '\r' + '\n'

    time.sleep(1)
    serCon.write(txtInASCII.encode("ASCII", "ignore"))



"""
