#!/usr/bin/env python3

from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep, time
import math
import sys

# Initialize the motors.
motor1 = Motor(OUTPUT_A)
motor2 = Motor(OUTPUT_B)
motor3 = Motor(OUTPUT_C)

# Initialize the sensors.
sensors = [UltrasonicSensor('in1'), UltrasonicSensor('in2'), UltrasonicSensor('in3'), UltrasonicSensor('in4')]

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
    motor1.on(f1 * 40)
    motor2.on(f2 * 40)
    motor3.on(f3 * 40)

# Calculate the forces to move straight forward.
F_foward = calculate_forces(1, 0, 0)
F_left = calculate_forces(0, -1, 0)
F_right = calculate_forces(0, 1, 0)
F_backward = calculate_forces(-1, 0, 0)

# Error threshold
error_threshold = 0.1  # Adjust this value as needed

# Direction variable
direction = 0  # 0 = forward, 1 = right, 2 = backward, 3 = left
last_direction = -1  # Initialize last direction as -1

# Flag to indicate if the robot is moving in a new direction
new_direction = False

# Main loop
while True:
    # Read the sensor values
    distances = [sensor.distance_centimeters for sensor in sensors]

    # If the front distance is less than 5 cm, stop and check left and right
    if distances[direction] < 5 and not new_direction:
        # Stop the robot
        motor1.off()
        motor2.off()
        motor3.off()

        # Pause for a moment
        sleep(1)

        # Check if there's space to the left or right
        possible_directions = [(direction + i) % 4 for i in range(-1, 2) if distances[(direction + i) % 4] > 10]
        if possible_directions:
            # Prefer to not go back in the same direction
            if last_direction in possible_directions:
                possible_directions.remove(last_direction)
            direction = possible_directions[0]
            if direction == (last_direction - 1) % 4:
                set_motor_speeds(*F_left)
            elif direction == (last_direction + 1) % 4:
                set_motor_speeds(*F_right)
            # Keep moving in the new direction until the robot is 5 cm away from a wall
            while distances[direction] > 5:
                # If the robot is too close to the left wall, move right
                if distances[1] < 6.5:  # Adjusted for sensor placement and maze dimensions
                    set_motor_speeds(*F_right)
                    sleep(0.2)  # Reduced sleep time for smoother adjustments
                # If the robot is too close to the right wall, move left
                if distances[3] < 6.5:  # Adjusted for sensor placement and maze dimensions
                    set_motor_speeds(*F_left)
                    sleep(0.2)  # Reduced sleep time for smoother adjustments
                sleep(0.1)  # Add a short delay to avoid excessive sensor readings
                distances = [sensor.distance_centimeters for sensor in sensors]  # Update distances
            new_direction = True
        else:
            break

    # If the robot is too close to the left wall, move right
    if distances[1] < 6.5:  # Adjusted for sensor placement and maze dimensions
        set_motor_speeds(*F_right)
        sleep(0.2)  # Reduced sleep time for smoother adjustments

    # If the robot is too close to the right wall, move left
    if distances[3] < 6.5:  # Adjusted for sensor placement and maze dimensions
        set_motor_speeds(*F_left)
        sleep(0.2)  # Reduced sleep time for smoother adjustments

    # Move forward
    set_motor_speeds(*F_foward)

    # Add a short delay to avoid excessive sensor readings
    sleep(0.1)

    # Update the last direction
    last_direction = direction

    # Reset the new direction flag if the robot has moved a sufficient distance in the new direction
    if new_direction and distances[direction] > 10:
        new_direction = False

# Stop the motors.
motor1.off()
motor2.off()
motor3.off()
