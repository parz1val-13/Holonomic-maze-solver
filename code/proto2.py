#!/usr/bin/env python3

from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep, time
import sys
from direction import Direction
import movement 
left_sensor = UltrasonicSensor('in4')
right_sensor = UltrasonicSensor('in2')
front_sensor = UltrasonicSensor('in1')
back_sensor = UltrasonicSensor('in3')

sensors = [front_sensor, back_sensor, left_sensor, right_sensor]
directions = [Direction.NORTH, Direction.SOUTH, Direction.WEST, Direction.EAST]

visited = set()
a = 0
b = 0
record_path = []
record_path.append((a,b))


def getCoordinate(x, y, direction):
    if direction == Direction.NORTH:
        return (x, y + 1)
    if direction == Direction.SOUTH:
        return (x, y - 1)
    if direction == Direction.EAST:
        return (x + 1, y)
    if direction == Direction.WEST:
        return (x - 1, y)
    

def moveInDirection(direction):

    global a
    global b
    if direction == Direction.NORTH:
        movement.moveForward()
        a = a + 1
    elif direction == Direction.SOUTH:
        movement.turnAround()
        a = a - 1
    elif direction == Direction.EAST:
        movement.turnRight()
        b = b + 1
    elif direction == Direction.WEST:
        movement.turnLeft()
        b = b - 1
    center_robot(direction)
    record = (a,b)
    record_path.append(record)


def moveOppositeDirection(direction):
    global a
    global b
    if direction == Direction.NORTH:
        movement.turnAround()
        a = a - 1        
    elif direction == Direction.SOUTH:
        movement.moveForward()
        a = a + 1
    elif direction == Direction.EAST:
        movement.turnLeft()  
        b = b - 1     
    elif direction == Direction.WEST:
        b = b + 1
        movement.turnRight()
    center_robot(direction)
    record = (a,b)
    record_path.append(record)

        
def center_robot(direction):
    if direction in [Direction.NORTH, Direction.SOUTH]:
        # Use sensors 2 and 4 to center
        left_distance = left_sensor.distance_centimeters_continuous
        right_distance = right_sensor.distance_centimeters_continuous
        if abs(left_distance - right_distance) > 1:
            if left_distance > right_distance and right_distance > 2:
                movement.adjustLeft()
            else:
                movement.adjustRight()
    elif direction in [Direction.EAST, Direction.WEST]:
        # Use sensors 1 and 3 to center
        front_distance = front_sensor.distance_centimeters_continuous
        back_distance = back_sensor.distance_centimeters_continuous
        if abs(front_distance - back_distance) > 1:
            if front_distance > back_distance and back_distance > 2:
                movement.adjustForward()
            else:
                movement.adjustAround()

def delete_between_coordinates(lst):
    i = 0
    while i < len(lst):
        current_coords = lst[i]
        # Find the next occurrence of the current coordinates
        j = i + 1
        while j < len(lst) and lst[j] != current_coords:
            j += 1

        # If a duplicate is found, delete everything between occurrences
        if j < len(lst):
            del lst[i + 1:j]

            # Move to the next occurrence for further processing
            i = j
        else:
            i += 1

    return lst

def getValidNeighbors(x, y):
    validDirections = []
    minDist = float(('inf'))
    for i in range(4):
        minDist = min(minDist, sensors[i].distance_centimeters)
        if sensors[i].distance_centimeters > 20:
            validDirections.append(directions[i])
    print('#####', file=sys.stderr)

    if minDist > 30:
        print('Solved the maze', file=sys.stderr)
        my_coordinates = record_path
        result = delete_between_coordinates(my_coordinates.copy())
        new_list = []

        for i in result:
            if i not in new_list:
                new_list.append(i)

        print(new_list, file=sys.stderr)
        ent = input("press t")
        if ent.lower() == 't':
            runner(0,0,new_list)
        
        exit()

    validNeighbors = []
    for dir in validDirections:
        x1, y1 = getCoordinate(x, y, dir)
        if (x1, y1) not in visited:
            validNeighbors.append((x1, y1, dir))

    return validNeighbors

def runner(a, b, mylist):
    for i in range(len(mylist) - 1):
        x, y = mylist[i]
        next_x, _ = mylist[i + 1]
        _, next_y = mylist[i + 1]
        
        if x > next_x:
            movement.turnLeft()
            direction = Direction.WEST
        elif x < next_x:
            movement.turnRight()
            direction = Direction.EAST
        if y > next_y:
            movement.turnAround()
            direction = Direction.SOUTH
        elif y < next_y:
            movement.moveForward()
            direction = Direction.NORTH
    center_robot(direction)


def dfs(x, y):
    global visited
    visited.add((x, y))
    #print(x, y, file=sys.stderr)

    for a, b, d in getValidNeighbors(x, y):
        print(record_path,file=sys.stderr)
        moveInDirection(d)
        dfs(a, b) 
        moveOppositeDirection(d)
    
def main():
    dfs(0, 0)


if __name__ == "__main__":
    main()
