#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 01:16:58 2019

@author: pi
"""

import RPi.GPIO as GPIO
import time

blight =25
glight =8
rlight =7

GPIO.setmode(GPIO.BCM)

GPIO.setup(rlight,GPIO.OUT)
GPIO.setup(glight,GPIO.OUT)
GPIO.setup(blight,GPIO.OUT)


while True:
    GPIO.output(rlight,True)
    time.sleep(1)
    GPIO.output(rlight,False)
    GPIO.output(blight,True)
    time.sleep(1)
    GPIO.output(blight,False)
    GPIO.output(glight,True)
    time.sleep(1)
    GPIO.output(glight,False)