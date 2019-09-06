#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 06:28:07 2019

@author: pi
"""

import RPi.GPIO as GPIO
import time

R,G,B=9,10,11
buzzer=16
GPIO.setmode(GPIO.BCM)

GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)

pwmR = GPIO.PWM(R, 70)
pwmG = GPIO.PWM(G, 70)
pwmB = GPIO.PWM(B, 70)

pwmR.start(0)
pwmG.start(0)  
pwmB.start(0)
4 kind of mode. It support more method.
try:
	t = 0.01
	while True:
       
        
            for i in range(0,71):
                pwmR.ChangeDutyCycle(0)
                pwmB.ChangeDutyCycle(71-i)
                pwmG.ChangeDutyCycle(i)
                print(1)
                time.sleep(t)
            for i in range(0,71):
                pwmR.ChangeDutyCycle(0)
                pwmB.ChangeDutyCycle(i)
                pwmG.ChangeDutyCycle(71-i)
                print(2)
                time.sleep(t)
            for i in range(0,71):
                pwmR.ChangeDutyCycle(i)
                pwmB.ChangeDutyCycle(71-i)
                pwmG.ChangeDutyCycle(0)
                print(1)
                time.sleep(t)
            for i in range(0,71):
                pwmR.ChangeDutyCycle(71-i)
                pwmB.ChangeDutyCycle(i)
                pwmG.ChangeDutyCycle(0)
                print(2)
                time.sleep(t)
          
except KeyboardInterrupt:
	pass
pwmR.stop()
pwmG.stop()
pwmB.stop()
GPIO.cleanup()
		                                                                                           
