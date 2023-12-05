#!/usr/bin/env python3

from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C
#from ev3dev2.motor import MoveTank, LargeMotor, OUTPUT_B, OUTPUT_C, MoveDifferential, SpeedRPM, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
from time import sleep, time
import math
import sys


# Initialize the motors.
motor1 = Motor(OUTPUT_A)
motor2 = Motor(OUTPUT_B)
motor3 = Motor(OUTPUT_C)

# Define the angles for each motor in radians.
a1 = math.radians(0)  # Motor 1 is at 0 degrees.
a2 = math.radians(150)  # Motor 2 is at 150 degrees.
a3 = math.radians(270)  # Motor 3 is at 270 degrees.

# Pre-calculated inverse matrix.
A_inv = [[0.56799, 0.34904, 0.33333], [-0.58627, 0.31738, 0.33333], [0.01827, -0.66642, 0.33333]]

# Function to calculate the forces.
def calculate_forces(ax, ay, ω):
    B = [ax, ay, ω]
    return [sum(A_inv[i][j] * B[j] for j in range(3)) for i in range(3)]

# Function to set the motor speeds.
def set_motor_speeds(f1, f2, f3):
    motor1.on(f1 * 50, 2)
    motor2.on(f2 * 50, 2)
    motor3.on(f3 * 50, 2)

# Calculate the forces to move straight forward.
F_foward = calculate_forces(1, 0, 0)
F_left = calculate_forces(0, -1, 0)
F_right = calculate_forces(0, 1, 0)
F_back = calculate_forces(-1, 0, 0)

def moveForward():
    set_motor_speeds(*F_foward)
    sleep(1.5)
    # Stop the motors.
    motor1.off()
    motor2.off()
    motor3.off()

def turnLeft():
    set_motor_speeds(*F_left)
    sleep(1.5)
    # Stop the motors.
    motor1.off()
    motor2.off()
    motor3.off()

def turnRight():
    set_motor_speeds(*F_right)
    sleep(1.5)
    # Stop the motors.
    motor1.off()
    motor2.off()
    motor3.off()

def turnAround():
    set_motor_speeds(*F_back)
    sleep(1.5)
    # Stop the motors.
    motor1.off()
    motor2.off()
    motor3.off()