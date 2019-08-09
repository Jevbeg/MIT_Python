# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 23:59:36 2019

@author: Alien
"""

import random

class stateLine:
    """Contains the state of line to be sent to the console."""
    
    DEFAULT_MODE = '#O'
    DEFAULT_CYCLE = 1
    DEFAULT_PPRESSURE = 2.2
    DEFAULT_OILPRESSURE = 3
    DEFAULT_GASPRESSURE = 10
    DEFAULT_TINT = 20
    DEFAULT_T1 = 20
    DEFAULT_GS = 2
    DEFAULT_TIME = 0
    DEFAULT_START = True
    MAX_TIME = 300
    
        
    def __init__(self, getMode = None):
        """Initializes the class instance."""
        
        if getMode is None :
            self.mode = self.DEFAULT_MODE
        else : self.mode = getMode
        
        self.cycle = self.DEFAULT_CYCLE
        self.pPressure = self.DEFAULT_PPRESSURE
        self.oilPressure = self.DEFAULT_OILPRESSURE
        self.gasPressure = self.DEFAULT_GASPRESSURE
        self.tInt = self.DEFAULT_TINT
        self.t1 = self.DEFAULT_T1
        self.gs = self.DEFAULT_GS
        self.time = self.DEFAULT_TIME
        self.start = self.DEFAULT_START

    def dataLine(self):
        """Returns line of actual data that is after the device operation mode."""
        
        dLine = b'\r' + b'\t' + \
                str(self.cycle).encode('ASCII') + b'\t' + \
                str(self.pPressure).encode('ASCII') + b'\t' + \
                str(self.oilPressure).encode('ASCII') + b'\t' + \
                str(self.gasPressure).encode('ASCII') + b'\t' + \
                str(self.tInt).encode('ASCII') + b'\t' + \
                str(self.t1).encode('ASCII') + b'\t' + \
                str(self.gs).encode('ASCII') + b'\t' + \
                str(self.time).encode('ASCII')
        return dLine
                
    def incrementLine(self):
        """Steps up in "Time" followed by a change in all parameters."""
        self.time += 1 
        self.pPressure = self.DEFAULT_PPRESSURE
        self.oilPressure = self.time // 3 * 2
        self.gasPressure += self.time // 299
        self.tInt += self.oilPressure // 195
        self.t1 = self.DEFAULT_T1
        self.gs = self.DEFAULT_GS
        

        
        
    def generateLine(self):
        """Generates the line for the console in a new mode or continuation"""
        """Uses stateLine.dataLine() for reference"""
        if self.start : 
#            generatedLine = str(self.mode).encode('ASCII') + b'\t' + \
#                            str(self.cycle).encode('ASCII') + \
#                            b' '*12 + \
#                            self.dataLine()
            generatedLine = b'\n' + b'\r' + \
                            str(self.mode).encode('ASCII') + b'\t' + \
                            str(self.cycle).encode('ASCII') + \
                            b' '*12 + \
                            self.dataLine()
            self.start = False
            
        else:
            
            self.incrementLine()
            generatedLine = self.dataLine()            
            if self.time == self.MAX_TIME : return None
            
        return generatedLine
    
    def continueFrom(self, stateLineObject) :
        """Is required for the mode to begin operation after switch"""
        self.start = self.DEFAULT_START
        
        self.cycle = stateLineObject.cycle
        self.pPressure = stateLineObject.pPressure
        self.oilPressure = self.DEFAULT_OILPRESSURE
        self.gasPressure = stateLineObject.oilPressure
        
        self.tInt = stateLineObject.tInt
        self.t1 = stateLineObject.t1
        self.gs = stateLineObject.gs
        self.time = self.DEFAULT_TIME  
                 

    
            