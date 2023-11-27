from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from time import sleep

left_sensor = ColorSensor('in1')
right_sensor = ColorSensor('in3')


target_intensity = 30
base_speed = 20
turn_speed = 40

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

while True:
    left_intensity = left_sensor.ambient_light_intensity
    right_intensity = right_sensor.ambient_light_intensity
    intensity_difference = left_intensity - right_intensity
    speed_difference = intensity_difference*0.1
    # Calculate the turn ratio to adjust the robot's direction
    turn_ratio = speed_difference / 100  # Adjust this value as needed
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



    
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from time import sleep

left_sensor = ColorSensor('in1')
right_sensor = ColorSensor('in3')


target_intensity = 20
base_speed = 10
turn_speed = 20

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

while True:
    left_intensity = left_sensor.ambient_light_intensity
    right_intensity = right_sensor.ambient_light_intensity
    intensity_difference = left_intensity - right_intensity
    speed_difference = intensity_difference * 5
    # Calculate the turn ratio to adjust the robot's direction
    turn_ratio = speed_difference / 100  # Adjust this value as needed
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