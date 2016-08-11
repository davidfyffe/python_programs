#!/usr/bin/env python
import DataBaseControllerFile
from DataBaseControllerFile import DatabaseController
import ServoControllerFile
from ServoControllerFile import ServoController
import time

dutyCycleFullRight = 3
dutyCycleFullLeft = 15
dutyCycleTDC = 8
dbController = DatabaseController()
servoController = ServoController(dutyCycleTDC)

def incrementAmount():
    currentValue = dbController.selectValue()
    if currentValue < dutyCycleFullLeft:
        currentValue += 1
        dbController.updateValue(currentValue)

        
def resetAmount():
    return dutyCycleTDC
    
def decrementAmount():
    currentValue = dbController.selectValue()
    if currentValue > dutyCycleFullRight:
        currentValue -= 1
        dbController.updateValue(currentValue)

def myCallBack(channel, increment):

    print "Edge detected on channel ", channel
    if increment == 'up':
        print "increment up"
        incrementAmount()
        #updateServoPosition(value)
    elif increment == 'down':
        print "increment down"
        decrementAmount()
        #updateServoPosition(value)
    else:
        print "reset servo"
        value = resetAmount()
        dbController.updateValue(value)
        #updateServoPosition(value)
        
def updateServoPosition(currentValue):
    #currentValue = dbController.selectValue()
    servoController.setServoToPosition(currentValue)
    
    

