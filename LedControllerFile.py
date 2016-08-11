#!/usr/bin/env python
import RPi.GPIO as GPIO # Remember to run as superuser (sudo)
import time

class LedController:
        
    'Common led controller class. takes pin number in constructor'
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        GPIO.setmode(GPIO.BCM)   # This example uses the BCM pin numbering
        GPIO.setup(self.gpio_pin, GPIO.OUT) # GPIO 25 is set to be an output.
        self.pwm = GPIO.PWM(self.gpio_pin, 50)   # pwm is an object. This gives a neat way to control the pin.
                             # 25 is the BCM pin number.
                             # 5 is the frequency in Hz.

    def light(self, beLight):
        if beLight == True:
            self.pwm.start(5.5)            
            self.pwm.ChangeDutyCycle(100)  # Duty cycle is now 50%
        else:                
            print("blue off")
            GPIO.output(self.gpio_pin, False)


    def flash(self, doFlash, sleeptime):
        if doFlash == True:
            self.pwm = GPIO.PWM(self.gpio_pin, 10)   # pwm is an object. This gives a neat way to control the pin.
                                 # 10 is the frequency in Hz.
            self.pwm.start(50)            # This 50 is the mark/space ratio or duty cycle of 50%
                                 # Values from 0 to 100 are allowed including numbers like 33.33
            time.sleep(sleeptime)            # Three seconds till the next change
            self.pwm.ChangeFrequency(50)  # Frequency is now 50 Hz - LED stops flickering
        else:
            print("50 at 50Hz")
            self.pwm.ChangeFrequency(50)# Frequency is now 50 Hz
            self.light(False)
            
       


#print LedController.__doc__

#c = LedController(22)
#c.flash(True, 0.5)
#c.light(True)
#time.sleep(5)
#c.flash(True)
#time.sleep(5)

