#!/usr/bin/env python3

from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep, time
import operator
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
    
def Move(value, mouse_coord):
    print(mouse_coord, file=sys.stderr)
    if value == 0 and mouse_coord not in coordinate_list or mouse_coord == [0,0]:
        movement.turnLeft()
        coordinate_list.append(mouse_coord)
    elif value == 1 and mouse_coord not in coordinate_list or mouse_coord == [0,0]:
        movement.turnRight()
        coordinate_list.append(mouse_coord)
    elif value == 2 :
        if mouse_coord not in coordinate_list or mouse_coord == [0,0]:
            movement.moveForward()
            coordinate_list.append(mouse_coord)
    elif value == 3 and mouse_coord not in coordinate_list or mouse_coord == [0,0]:
        movement.turnAround()
        coordinate_list.append(mouse_coord)
    
def main():
    x,y = 0,0
    Mouse_init = [x, y]    
    coordinate_list.append(Mouse_init)


    while abs(x) < 3 or abs(y) < 3:
       # print(Mouse_init, file=sys.stderr)
        all_sensors = [left_sensor.distance_centimeters, right_sensor.distance_centimeters,front_sensor.distance_centimeters, back_sensor.distance_centimeters]
        temp_x = Mouse_init[0]
        temp_y = Mouse_init[1]
        distance_check = 20
        max_i = 0
        max_dist = -1
      #  print(all_sensors, file=sys.stderr)
        for i in range(len(all_sensors)):
            if all_sensors[i] > max_dist:
             max_dist = all_sensors[i]
             max_i=i
        print( max_i, file=sys.stderr)
        sleep(2)
        Move(max_i, Mouse_init)
        '''
        if left_sensor.distance_centimeters > distance_check or right_sensor.distance_centimeters > 10:
            if left_sensor.distance_centimeters > right_sensor.distance_centimeters:
                Mouse_init = getNeighbor(Mouse_init, Direction.WEST)
            elif left_sensor.distance_centimeters < right_sensor.distance_centimeters:
                Mouse_init = getNeighbor(Mouse_init, Direction.EAST)

            if x < temp_x and Mouse_init not in coordinate_list and x > -1:
                movement.turnLeft()
            elif x > temp_x and Mouse_init not in coordinate_list and x > -1:
                 movement.turnRight()


        if front_sensor.distance_centimeters > 10 or back_sensor.distance_centimeters > 10:
            if front_sensor.distance_centimeters > back_sensor.distance_centimeters:
                Mouse_init = getNeighbor(Mouse_init, Direction.NORTH)
            elif front_sensor.distance_centimeters < back_sensor.distance_centimeters:
                Mouse_init = getNeighbor(Mouse_init, Direction.SOUTH)
            
            if y > temp_y and Mouse_init not in coordinate_list and y > -1:
                movement.moveForward()
            elif y < temp_y and Mouse_init not in coordinate_list and y> -1:
                 movement.turnAround()
                '''


'''
        if left_sensor.distance_centimeters < 10 and right_sensor.distance_centimeters < 10 and front_sensor.distance_centimeters > 10:
        if left_sensor.distance_centimeters > 10:

            Mouse_init = getNeighbor(Mouse_init, Direction.WEST)
            if Mouse_init not in coordinate_list: 
                movement.turnLeft()
                coordinate_list.append(Mouse_init)
            else:
                continue

        elif right_sensor.distance_centimeters > 10:
            
            Mouse_init = getNeighbor(Mouse_init, Direction.EAST)
            if Mouse_init not in coordinate_list:
                movement.turnRight()
                coordinate_list.append(Mouse_init)
            else:
                continue

        elif front_sensor.distance_centimeters > 10:

            Mouse_init = getNeighbor(Mouse_init, Direction.NORTH)
            if Mouse_init not in coordinate_list:
                movement.moveForward()
                print(Mouse_init, file=sys.stderr)
                coordinate_list.append(Mouse_init)
            else:
                continue
            
        elif back_sensor.distance_centimeters > 10:
            Mouse_init = getNeighbor(Mouse_init, Direction.SOUTH)
            if Mouse_init not in coordinate_list:
                movement.turnAround()
                coordinate_list.append(Mouse_init)
            else:
                continue
           
        else:
            Mouse_init = getNeighbor(Mouse_init, Direction.EAST)
            coordinate_list.append(Mouse_init)
                '''  
#print("broken", file=sys.stderr)
if __name__ == "__main__":
    main()