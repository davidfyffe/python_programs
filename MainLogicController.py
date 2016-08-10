#!/usr/bin/env python
import DataBaseControllerFile
from DataBaseControllerFile import DatabaseController
import ServoControllerFile
from ServoControllerFile import ServoController


dutyCycleFullRight = 3
dutyCycleFullLeft = 15
dutyCycleTDC = 9
dbController = DatabaseController()
servoController = ServoController()

def incrementAmount(currentPosition):
    if currentPosition < dutyCycleFullLeft:
        currentPosition += 1
        return currentPosition
    else:
        return currentPosition
        
def resetAmount():
    return dutyCycleTDC
    
def decrementAmount(currentPosition):
    if currentPosition > dutyCycleFullRight:
        currentPosition -= 1
        return currentPosition
    else:
        return currentPosition

def myCallBack(channel, increment):

    print "Edge detected on channel ", channel
    if increment == 'up':
        print "increment up"
        #increment the db
        #get current pos from db
        currentValue = dbController.selectValue()
        value = incrementAmount(currentValue)
        dbController.updateValue(value)
        updateServoPosition(value)
    elif increment == 'down':
        print "increment down"
        #increment the db
        #get current pos from db
        currentValue = dbController.selectValue()
        value = decrementAmount(currentValue)
        dbController.updateValue(value)
        updateServoPosition(value)
    else:
        print "reset servo"
        value = resetAmount()
        dbController.updateValue(value)
        updateServoPosition(value)
        
def updateServoPosition(position):
    servoController.setServoToPosition(position)
