# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 23:59:36 2019

@author: Alien
"""

class stateLine:
    """Contains the state state of line to be sent to the console."""
    
    DEFAULT_MODE = '#O'
    DEFAULT_CYCLE = 1
    DEFAULT_PPRESSURE = 1.0
    DEFAULT_OILPRESSURE = 1
    DEFAULT_GASPRESSURE = 1
    DEFAULT_TINT = 20
    DEFAULT_T1 = 20
    DEFAULT_GS = 2
    DEFAUT_TIME = 0
    
        
    def __init__(self):
    
        
    def generateLine(self, startAnew):
        
        if startAnew : 
             generatedLine = self.mode + b'\t' + self.cycle + b' '*12 + \
        
        return generatedLine
            