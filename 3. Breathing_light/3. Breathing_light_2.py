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

pwmR = GPIO.PWM(R, 70)
pwmG = GPIO.PWM(G, 70)
pwmB = GPIO.PWM(B, 70)
pwmR.start(0)
pwmG.start(0)  
pwmB.start(0)

try:
	t = 0.01
	while True:
            
            for i in range(0,71):
                pwmG.ChangeDutyCycle(i)
                time.sleep(t)
            for i in range(70,-1,-1):
                pwmG.ChangeDutyCycle(i)
                time.sleep(t)
            for i in range(0,71):
                pwmR.ChangeDutyCycle(i)
                time.sleep(t)
            for i in range(70,-1,-1):
                pwmR.ChangeDutyCycle(i)
                time.sleep(t)
            for i in range(0,71):
                pwmB.ChangeDutyCycle(i)
                time.sleep(t)
            for i in range(70,-1,-1):
                pwmB.ChangeDutyCycle(i)
                time.sleep(t)        
except KeyboardInterrupt:
	pass
pwmR.stop()
pwmG.stop()
pwmB.stop()
GPIO.cleanup()
		                                                                                           
