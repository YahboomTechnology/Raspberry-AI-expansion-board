#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 07:51:54 
Shenzhen Yahboom Tech

@author: LONGFU SUN
"""

import RPi.GPIO as GPIO
import time
LEDBlue=20
LEDYellow=21

GPIO.setmode(GPIO.BCM)

GPIO.setup(LEDBlue,GPIO.OUT)
GPIO.setup(LEDYellow,GPIO.OUT)

while True:
    GPIO.output(LEDBlue,True)
    time.sleep(0.5)
    GPIO.output(LEDBlue,False)
    GPIO.output(LEDYellow,True)
    time.sleep(0.5)
    GPIO.output(LEDYellow,False)

