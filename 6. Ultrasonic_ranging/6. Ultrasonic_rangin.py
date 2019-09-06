#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:08:58 2019

@author: pi
"""
import RPi.GPIO as GPIO
import time
trig= 23
echo=24

GPIO.setmode(GPIO.BCM)
GPIO.setup(trig,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(echo,GPIO.IN)

time.sleep(2)

def distance():
    GPIO.output(trig,GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(trig,GPIO.LOW)
    while not GPIO.input(echo):
        pass
    t1=time.time()
    while GPIO.input(echo):
        pass
    t2=time.time()
    print((t2-t1)*340*100/2)
    

try:
    while True:
        distance()
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()