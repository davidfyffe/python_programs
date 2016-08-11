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
            print("blue on")
            self.pwm.start(5.5)
            #self.pwm.ChangeFrequency(10) # Frequency is now 5.5 Hz
            self.pwm.ChangeDutyCycle(100)  # Duty cycle is now 50%
            #GPIO.output(self.gpio_pin, True)
        else:                
            print("blue off")
            GPIO.output(self.gpio_pin, False)


    def flash(self, doFlash):
        if doFlash == True:
            self.light(True)
            print("50 at 5.5Hz")
            #self.pwm.start(10)
            self.pwm.ChangeFrequency(10) # Frequency is now 5.5 Hz
            self.pwm.ChangeDutyCycle(100)  # Duty cycle is now 50%
        else:
            print("50 at 50Hz")
            self.pwm.ChangeFrequency(50)# Frequency is now 50 Hz
            self.light(False)
    

#print LedController.__doc__

#c = LedController(23)
#c.light(True)
#time.sleep(5)
#c.flash(True)
#time.sleep(5)

