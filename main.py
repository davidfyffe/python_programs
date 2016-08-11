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

import MainLogicController as mainController

import DataBaseControllerFile
from DataBaseControllerFile import DatabaseController


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
    

    blueLed.light(True);
    redLed.light(True);
    greenLed.light(True);

    
    redButton.registerForButtonEvent()
    blueButton.registerForButtonEvent()
    greenButton.registerForButtonEvent()
   
    db = DatabaseController()
    while True:
        value = db.selectValue()
        mainController.updateServoPosition(value)
        time.sleep(0.25)
                
    return 0

if __name__ == '__main__':
	main()

