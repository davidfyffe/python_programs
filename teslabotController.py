#!/usr/bin/env python
import time
#import MainLogicController as mainlogic
import LedControllerFile
from LedControllerFile import LedController
import thread
import DataBaseControllerFile
from DataBaseControllerFile import DatabaseController
import ServoControllerFile
from ServoControllerFile import ServoController
import espeak as talker

BLUELED = 22
REDLED = 23
GREENLED = 24


    
def flashBlue():
    print "Starting flash blue"
    blueLed = LedController(BLUELED)
    blueLed.flash(True, 5)
    blueLed.light(True)
    
def flashRed():
    print "Starting flash red"
    redLed = LedController(REDLED)
    redLed.flash(True, 5)
    redLed.light(True)
    
def flashGreen():
    print "Starting flash green"
    greenLed = LedController(GREENLED)
    greenLed.flash(True, 5)
    greenLed.light(True)

def flashAll():
    thread.start_new_thread(flashBlue, ())
    thread.start_new_thread(flashRed, ())
    thread.start_new_thread(flashGreen, ())
    
def gonuts():
    flashAll()
    db = DatabaseController()
    sc = ServoController(8)
    counter =0
    while counter <= 2:
        counter += 1
        for angle in range(3, 15):
            #db.updateValue(angle
            sc.setServoToPosition(angle)
            time.sleep(0.05)

        for angle in range(3, 15):
            sc.setServoToPosition(15-angle)
            #db.updateValue(15 -angle) 
            time.sleep(0.05)

def speak(text):
    talker.say(text)            
#gonuts()
#flashAll()
