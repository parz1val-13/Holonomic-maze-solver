#!/usr/bin/env python3

from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep, time
import math
import sys
from direction import Direction
import movement 
left_sensor = UltrasonicSensor('in4')
right_sensor = UltrasonicSensor('in2')
front_sensor = UltrasonicSensor('in1')
back_sensor = UltrasonicSensor('in3')

while True:
    print(back_sensor.distance_centimeters, file=sys.stderr)
    sleep(1);