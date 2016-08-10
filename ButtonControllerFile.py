#!/usr/bin/env python
import RPi.GPIO as GPIO # Remember to run as superuser (sudo)
import time
import MainLogicController as mainlogic


class ButtonController:
    'Common button controller class. takes pin number in constructor'
    def __init__(self, gpio_pin, increment):
        self.gpio_pin = gpio_pin
        self.increment = increment
        GPIO.setmode(GPIO.BCM)   # This example uses the BCM pin numbering
        GPIO.setup(self.gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def checkForButtonPress(self):
        input_state = GPIO.input(self.gpio_pin)
        if input_state == False:
            print "Button Pressed on ", self.gpio_pin
            time.sleep(0.2)
        
    def registerForButtonEvent(self):
        GPIO.add_event_detect(self.gpio_pin, GPIO.RISING, callback=self.myCallBack)
    
    #local callback defering logic to main controller
    def myCallBack(self, channel):
        mainlogic.myCallBack(channel, self.increment)
    
        
        
#print ButtonController.__doc__

#c = ButtonController(22, 'up')
#c.registerForButtonEvent()
