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
    if direction == Direction.NORTH:
        movement.moveForward()
    elif direction == Direction.SOUTH:
        movement.turnAround()
    elif direction == Direction.EAST:
        movement.turnRight()
    elif direction == Direction.WEST:
        movement.turnLeft()
    center_robot(direction)


def moveOppositeDirection(direction):
    if direction == Direction.NORTH:
        movement.turnAround()        
    elif direction == Direction.SOUTH:
        movement.moveForward()
    elif direction == Direction.EAST:
        movement.turnLeft()       
    elif direction == Direction.WEST:
        movement.turnRight()
    center_robot(direction)
        
def center_robot(direction):
    if direction in [Direction.NORTH, Direction.SOUTH]:
        # Use sensors 2 and 4 to center
        while abs(left_sensor.distance_centimeters - right_sensor.distance_centimeters) > 1:
            if left_sensor.distance_centimeters > right_sensor.distance_centimeters:
                if right_sensor.distance_centimeters < 2:
                    break
                movement.adjustRight()
                sleep(0.1)  # Allow some time for the robot to adjust
                left_sensor.distance_centimeters = left_sensor.distance_centimeters_continuous
                right_sensor.distance_centimeters = right_sensor.distance_centimeters_continuous
            else:
                if left_sensor.distance_centimeters < 2:
                    break
                movement.adjustLeft()
                sleep(0.1)  # Allow some time for the robot to adjust
                left_sensor.distance_centimeters = left_sensor.distance_centimeters_continuous
                right_sensor.distance_centimeters = right_sensor.distance_centimeters_continuous
    elif direction in [Direction.EAST, Direction.WEST]:
        # Use sensors 1 and 3 to center
        while abs(front_sensor.distance_centimeters - back_sensor.distance_centimeters) > 1:
            if front_sensor.distance_centimeters > back_sensor.distance_centimeters:
                if back_sensor.distance_centimeters < 2:
                    break
                movement.adjustForward()
                sleep(0.1)  # Allow some time for the robot to adjust
                front_sensor.distance_centimeters = front_sensor.distance_centimeters_continuous
                back_sensor.distance_centimeters = back_sensor.distance_centimeters_continuous
            else:
                if front_sensor.distance_centimeters < 2:
                    break
                movement.adjustAround()
                sleep(0.1)  # Allow some time for the robot to adjust
                front_sensor.distance_centimeters = front_sensor.distance_centimeters_continuous
                back_sensor.distance_centimeters = back_sensor.distance_centimeters_continuous



def getValidNeighbors(x, y):
    validDirections = []
    print('#####', file=sys.stderr)
    minDist = float(('inf'))
    for i in range(4):
        print(sensors[i].distance_centimeters, file=sys.stderr)
        minDist = min(minDist, sensors[i].distance_centimeters)
        if sensors[i].distance_centimeters > 20:
            validDirections.append(directions[i])
    print('#####', file=sys.stderr)

    if minDist > 30:
        print('Solved the maze', file=sys.stderr)
        exit()

    validNeighbors = []
    for dir in validDirections:
        x1, y1 = getCoordinate(x, y, dir)
        if (x1, y1) not in visited:
            validNeighbors.append((x1, y1, dir))

    return validNeighbors


def dfs(x, y):
    global visited
    visited.add((x, y))
    print(x, y, file=sys.stderr)

    for a, b, d in getValidNeighbors(x, y):
        moveInDirection(d)
        dfs(a, b) 
        moveOppositeDirection(d)
  
    
def main():
    dfs(0, 0)


if __name__ == "__main__":
    main()