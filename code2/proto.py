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

    while abs(x) < 8 or abs(y) < 8:
        
        if left_sensor.distance_centimeters > 10:
            if front_sensor.distance_centimeters < 3:
                while abs(front_sensor.distance_centimeters - back_sensor.distance_centimeters) > 1:
                    movement.turnAround()
                    sleep(0.2)
            if back_sensor.distance_centimeters < 3:
                while abs(back_sensor.distance_centimeters - front_sensor.distance_centimeters) > 1:
                    movement.moveForward()
                    sleep(0.2)
            Mouse_neighbor = getNeighbor(Mouse_init, Direction.WEST)
            if Mouse_neighbor not in coordinate_list: 
                movement.turnLeft()
                coordinate_list.append(Mouse_neighbor)
                Mouse_init = Mouse_neighbor
            else:
                continue

        elif right_sensor.distance_centimeters > 10:
            if front_sensor.distance_centimeters < 3:
                while abs(front_sensor.distance_centimeters - back_sensor.distance_centimeters) > 1:
                    movement.turnAround()
                    sleep(0.2)
            if back_sensor.distance_centimeters < 3:
                while abs(back_sensor.distance_centimeters - front_sensor.distance_centimeters) > 1:
                    movement.moveForward()
                    sleep(0.2)
            Mouse_neighbor = getNeighbor(Mouse_init, Direction.EAST)
            if Mouse_neighbor not in coordinate_list:
                movement.turnRight()
                coordinate_list.append(Mouse_neighbor)
                Mouse_init = Mouse_neighbor
            else:
                continue

        elif front_sensor.distance_centimeters > 10:
            print("hahagagagagaga", file=sys.stderr)
            if left_sensor.distance_centimeters < 3:
                while abs(left_sensor.distance_centimeters - right_sensor.distance_centimeters) > 1:
                    movement.turnRight()
                    sleep(0.2)
            if right_sensor.distance_centimeters < 3:
                while abs(right_sensor.distance_centimeters - left_sensor.distance_centimeters) > 1:
                    movement.turnLeft()
                    sleep(0.2)
            print("hahagagagagaga", file=sys.stderr)
            Mouse_neighbor = getNeighbor(Mouse_init, Direction.NORTH)
            print(coordinate_list, file=sys.stderr)
            print(Mouse_neighbor, file=sys.stderr)
            #print("hahagagagagaga", file=sys.stderr)
            if Mouse_neighbor not in coordinate_list:
                movement.moveForward()
                print(Mouse_neighbor, file=sys.stderr)
                #print("hahagagagagaga", file=sys.stderr)

                coordinate_list.append(Mouse_neighbor)
                Mouse_init = Mouse_neighbor
            else:
                continue
            
        elif back_sensor.distance_centimeters > 10:
            if left_sensor.distance_centimeters < 3:
                while abs(left_sensor.distance_centimeters - right_sensor.distance_centimeters) > 1:
                    movement.turnRight()
                    sleep(0.2)
            if right_sensor.distance_centimeters < 3:
                while abs(right_sensor.distance_centimeters - left_sensor.distance_centimeters) > 1:
                    movement.turnLeft()
                    sleep(0.2)
            Mouse_neighbor = getNeighbor(Mouse_init, Direction.SOUTH)
            if Mouse_neighbor not in coordinate_list:
                movement.turnAround()
                coordinate_list.append(Mouse_neighbor)
                Mouse_init = Mouse_neighbor
            else:
                continue
            
        else:
            Mouse_init = getNeighbor(Mouse_init, Direction.EAST)
            coordinate_list.append(Mouse_init)
        
    #movement.moveForward()
    #movement.moveForward()
    print("broken", file=sys.stderr)
if __name__ == "__main__":
    main()