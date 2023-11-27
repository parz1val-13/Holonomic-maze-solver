#!/usr/bin/env python3

'''from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
import math

# Define your wheel parameters (in millimeters)
wheel_diameter = 56  # Replace with your wheel diameter
track_width = 180   # Replace with your track width

# Specify the diameter of the circular path (50mm)
circle_diameter = 200

# Calculate the radius from the diameter
circle_radius = circle_diameter / 2.0

# Calculate the circumference of the wheel
wheel_circumference = math.pi * wheel_diameter

# Calculate the circumference of the circle
circle_circumference = math.pi * circle_diameter

# Calculate the number of rotations for one lap of the circle
circle_rotations = circle_circumference / wheel_circumference

# Calculate the speed for both motors (adjust as needed)
speed_left = 30  # Adjust left motor speed
speed_right = (circle_radius / (circle_radius + (track_width / 2))) * 30  # Adjust right motor speed

# Initialize the motors
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

turn_distance = ( math.pi * track_width) / 6

revolutions = turn_distance / wheel_circumference

# Start turning in an arc for one full circle
tank_drive.on_for_rotations(left_speed=speed_left, right_speed=speed_right, rotations=circle_rotations * 2)

tank_drive.on_for_rotations(25, -25, revolutions)

tank_drive.on_for_seconds(30,30,5.1)

tank_drive.on_for_rotations(-25, 25, revolutions)

tank_drive.on_for_rotations(left_speed=speed_right, right_speed=speed_left, rotations=circle_rotations * 1.9)

turn_distance = ( math.pi * track_width) / 8

revolutions = turn_distance / wheel_circumference

tank_drive.on_for_rotations(-25, 25, revolutions)

tank_drive.on_for_seconds(30,30,5)

turn_distance = ( math.pi * track_width) / 6

revolutions = turn_distance / wheel_circumference

tank_drive.on_for_rotations(25, -25, revolutions)


# Close the motors
tank_drive.off()'''

from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from time import sleep
import sys


def Cowardice():
    left_sensor = ColorSensor('in1')
    right_sensor = ColorSensor('in3')
    base_speed = 15
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

    while True:
        left_intensity = left_sensor.ambient_light_intensity
        right_intensity = right_sensor.ambient_light_intensity
        intensity_difference = left_intensity - right_intensity
        speed_difference = intensity_difference * 5
        # Calculate the turn ratio to adjust the robot's direction
        # Calculate the left and right motor speeds
        left_speed = base_speed + speed_difference
        right_speed = base_speed - speed_difference

        # Limit the motor speeds to prevent them from going beyond the allowed range
        left_speed = max(-100, min(100, left_speed))
        right_speed = max(-100, min(100, right_speed))

        # Set the motor speeds
        if abs(intensity_difference) > 15:
            tank_drive.on_for_seconds(-70, -70, .4)
        else:

            tank_drive.on(-left_speed, -right_speed)

        # Sleep for a short time to avoid excessive CPU usage
        sleep(0.1)

def Aggression():
    left_sensor = ColorSensor('in1')
    right_sensor = ColorSensor('in3')
    base_speed = 10

    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

    while True:
        left_intensity = left_sensor.ambient_light_intensity
        right_intensity = right_sensor.ambient_light_intensity
        intensity_difference = left_intensity - right_intensity
        speed_difference = intensity_difference * 5
        # Calculate the left and right motor speeds
        left_speed = base_speed - speed_difference
        right_speed = base_speed + speed_difference

        # Limit the motor speeds to prevent them from going beyond the allowed range
        left_speed = max(-100, min(100, left_speed))
        right_speed = max(-100, min(100, right_speed))

        # Set the motor speeds
        tank_drive.on(left_speed, right_speed)

        # Sleep for a short time to avoid excessive CPU usage
        sleep(0.1)

Aggression()