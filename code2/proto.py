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

coordinate_list = []



def getNeighbor(position, direction):
    x, y = position
    if direction == Direction.NORTH:
        return (x, y + 1)
    if direction == Direction.SOUTH:
        return (x, y - 1)
    if direction == Direction.EAST:
        return (x + 1, y)
    if direction == Direction.WEST:
        return (x - 1, y)
    
def main():


    x,y = 0,0
    Mouse_init = (x, y)
    coordinate_list.append(Mouse_init)
    while x != 7 or y != 7:
        print(Mouse_init)
        if left_sensor.distance_centimeters > 10:
            Mouse_init = getNeighbor(Mouse_init, Direction.WEST)
            coordinate_list.append(Mouse_init)
            if front_sensor.distance_centimeters < 3:
                while abs(front_sensor.distance - back_sensor.distance) > 1:
                    movement.turnAround()
            if back_sensor.distance_centimeters < 3:
                while abs(back_sensor.distance - front_sensor.distance) > 1:
                    movement.moveFoward()
            movement.turnLeft()
        elif right_sensor.distance_centimeters > 10:
            Mouse_init = getNeighbor(Mouse_init, Direction.EAST)
            coordinate_list.append(Mouse_init)
            if front_sensor.distance_centimeters < 3:
                while abs(front_sensor.distance - back_sensor.distance) > 1:
                    movement.turnAround()
            if back_sensor.distance_centimeters < 3:
                while abs(back_sensor.distance - front_sensor.distance) > 1:
                    movement.moveFoward()
            movement.turnRight()
        elif front_sensor.distance_centimeters > 10:
            Mouse_init = getNeighbor(Mouse_init, Direction.NORTH)
            coordinate_list.append(Mouse_init)
            if left_sensor.distance_centimeters < 3:
                while abs(left_sensor.distance - right_sensor.distance) > 1:
                    movement.turnRight()
            if right_sensor.distance_centimeters < 3:
                while abs(right_sensor.distance - left_sensor.distance) > 1:
                    movement.turnLeft()
            movement.moveForward()
        elif back_sensor.distance_centimeters > 10:
            Mouse_init = getNeighbor(Mouse_init, Direction.SOUTH)
            coordinate_list.append(Mouse_init)
            if left_sensor.distance_centimeters < 3:
                while abs(left_sensor.distance - right_sensor.distance) > 1:
                    movement.turnRight()
            if right_sensor.distance_centimeters < 3:
                while abs(right_sensor.distance - left_sensor.distance) > 1:
                    movement.turnLeft()
            movement.turnAround()
        else:
            Mouse_init = getNeighbor(Mouse_init, Direction.EAST)
            coordinate_list.append(Mouse_init)
        
    movement.moveForward()
    movement.moveForward()
if __name__ == "__main__":
    main()