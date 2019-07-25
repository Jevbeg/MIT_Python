# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 23:59:36 2019

@author: Alien
"""

import random

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
        """Initializes the class instance."""
        self.mode = self.DEFAULT_MODE
        self.cycle = self.DEFAULT_CYCLE
        self.pPressure = self.DEFAULT_PPRESSURE
        self.oilPressure = self.DEFAULT_OILPRESSURE
        self.gasPressure = self.DEFAULT_GASPRESSURE
        self.tInt = self.DEFAULT_TINT
        self.t1 = self.DEFAULT_T1
        self.gs = self.DEFAULT_GS
        self.time = self.DEFAUT_TIME

    def dataLine(self):
        """Returns line of actual data that is after the mode."""
        
        dLine = b'\r' + b't' + \
                       str(self.cycle).encode('ASCII') + b't' + \
                       str(self.pPressure).encode('ASCII') + b't' + \
                       str(self.oilPressure).encode('ASCII') + b't' + \
                       str(self.gasPressure).encode('ASCII') + b't' + \
                       str(self.tInt).encode('ASCII') + b't' + \
                       str(self.t1).encode('ASCII') + b't' + \
                       str(self.gs).encode('ASCII') + b't' + \
                       str(self.time).encode('ASCII')
        return dLine
                
    def incrementLine(self, cycleTime):
        """Steps up in "Time" followed by a change in all parameters."""
        self.time = cycleTime
         
                           
        
        
    def generateLine(self, startAnew):
        """Generates the line for the console in a new mode or continuation"""
        if startAnew : 
            generatedLine = self.mode + b'\t' + \
                            self.cycle + \
                            b' '*12 + \
                            self.dataLine()
            
        else:
            self.incrementLine()
            generatedLine = self.dataLine()
        
        return generatedLine                    

    
            