#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
        
class ServoController:
    'Common servo controller class.'
    
    def __init__(self):
        
        self.pwm = GPIO.PWM(18, 50) #50Hz
        #DutyCycle to 5%  Full Left
        

    def setServoToPosition(self, position):
        print "ServoController: Setting position to ", position
        self.pwm.ChangeDutyCycle(position)        
        self.pwm.stop()
        GPIO.cleanup()
