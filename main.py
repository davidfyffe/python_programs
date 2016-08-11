#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2016  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
import time
import LedControllerFile
from LedControllerFile import LedController

import ButtonControllerFile
from ButtonControllerFile import ButtonController



def main():
    
    BLUELED = 22
    BLUESWITCH = 27
    REDLED = 23
    REDSWITCH = 25
    GREENLED = 24
    GREENSWITCH = 6
	
    blueLed = LedController(BLUELED)
    blueButton = ButtonController(BLUESWITCH, 'reset')
    redLed = LedController(REDLED)
    redButton = ButtonController(REDSWITCH, 'down')
    greenLed = LedController(GREENLED)
    greenButton = ButtonController(GREENSWITCH, 'up')
    
    #print "BLUE LED"
    blueLed.light(True);
    #blueLed.light(False);
    #blueLed.flash(True);
    #time.sleep(3)
    
    #blueLed.flash(False);
    
    #print "RED LED"
    redLed.light(True);
    #redLed.light(False);
    #redLed.flash(True);
    #redLed.flash(False);
    
    #print "RED LED"
    greenLed.light(True);
    #greenLed.light(False);
    #greenLed.flash(True);
    #greenLed.flash(False);
    
    redButton.registerForButtonEvent()
    blueButton.registerForButtonEvent()
    greenButton.registerForButtonEvent()
    #redButton.myCallBack(REDSWITCH)
    #greenButton.myCallBack(GREENSWITCH)
    #blueButton.myCallBack(BLUESWITCH)
    
    while True:
        print "doing nothing"
        time.sleep(10)
        
    return 0

if __name__ == '__main__':
	main()

