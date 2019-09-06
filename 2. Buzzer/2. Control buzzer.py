#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 10:01:05 2019

@author: pi
"""

import RPi.GPIO as GPIO
import time

buzzer=16

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer,GPIO.OUT)


while True:
    GPIO.output(buzzer,True)
    time.sleep(0.2)
    GPIO.output(buzzer,False)
    time.sleep(0.2)