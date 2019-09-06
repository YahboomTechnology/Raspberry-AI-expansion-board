#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 07:51:54 
Shenzhen Yahboom Tech

@author: LONGFU SUN
"""

from __future__ import division
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

mA1=8
mA2=9
mB1=10
mB2=11

pwm.set_pwm_freq(50)


#Maximum frequency is 4096, 4096, the highest speed, 1024, 2048, 3072
#forward, two servos rotate in the same direction
def forward():
    pwm.set_pwm(mA1,0,1024)
    pwm.set_pwm(mA2,0,0)
    pwm.set_pwm(mB1,0,1024)
    pwm.set_pwm(mB2,0,0)
    time.sleep(1)
#back，two servo rotate in the opposite direction of forward()
def back():
    pwm.set_pwm(mA2,0,1024)
    pwm.set_pwm(mA1,0,0)
    pwm.set_pwm(mB2,0,1024)
    pwm.set_pwm(mB1,0,0)
    time.sleep(1)
#Spin_left, give the right servo forward speed, and give the left servo backward speed.
def spin_left():
    pwm.set_pwm(mA1,0,0)
    pwm.set_pwm(mA2,0,1024)
    pwm.set_pwm(mB1,0,1024)
    pwm.set_pwm(mB2,0,0)
    time.sleep(1)
#Spin_right, give the left servo forward speed, and give the right servo backward speed.
def spin_right():
    pwm.set_pwm(mA1,0,1024)
    pwm.set_pwm(mA2,0,0)
    pwm.set_pwm(mB1,0,0)
    pwm.set_pwm(mB2,0,1024)
    time.sleep(1)
#Turn left，change the servo angle by the frequency difference
def left():
    pwm.set_pwm(mA1,0,512)
    pwm.set_pwm(mA2,0,0)
    pwm.set_pwm(mB1,0,1024)
    pwm.set_pwm(mB2,0,0)
    time.sleep(1)
#Turn right，change the servo angle by the frequency difference
def right():
    pwm.set_pwm(mA1,0,1024)
    pwm.set_pwm(mA2,0,0)
    pwm.set_pwm(mB1,0,512)
    pwm.set_pwm(mB2,0,0)
    time.sleep(1)
def stop():
    pwm.set_pwm(mA1,0,0)
    pwm.set_pwm(mA2,0,0)
    pwm.set_pwm(mB1,0,0)
    pwm.set_pwm(mB2,0,0)
    time.sleep(1)
#Delay 
for i in range(0,10):
    forward()
    time.sleep(1)
    back()
    time.sleep(1)
    spin_left()
    time.sleep(1)
    spin_right()
    time.sleep(1)
    stop()
    

print('Moving servo on channel 0, press Ctrl-C to quit...')