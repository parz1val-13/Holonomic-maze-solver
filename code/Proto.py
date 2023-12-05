from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep, time
import math
import sys
from Direction import Direction
from Movement import Movement
left_sensor = UltrasonicSensor('in1')
right_sensor = UltrasonicSensor('in3')
front_sensor = UltrasonicSensor('in2')
back_sensor = UltrasonicSensor('in4')

coordinate_list = []

Mouse_init = (0,0)

coordinate_list.append(Mouse_init)

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

    while Mouse_init.x != 7 or Mouse_init.y != 7:
        if left_sensor.distance_centimeters < 10:
            Mouse_init = getNeighbor(Mouse_init, Direction.WEST)
            coordinate_list.append(Mouse_init)
            Movement.turnLeft()
        elif right_sensor.distance_centimeters < 10:
            Mouse_init = getNeighbor(Mouse_init, Direction.EAST)
            coordinate_list.append(Mouse_init)
            Movement.turnRight()
        elif front_sensor.distance_centimeters < 10:
            Mouse_init = getNeighbor(Mouse_init, Direction.NORTH)
            coordinate_list.append(Mouse_init)
            Movement.moveForward()
        elif back_sensor.distance_centimeters < 10:
            Mouse_init = getNeighbor(Mouse_init, Direction.SOUTH)
            coordinate_list.append(Mouse_init)
            Movement.turnAround()
        else:
            Mouse_init = getNeighbor(Mouse_init, Direction.EAST)
            coordinate_list.append(Mouse_init)


if __name__ == "__main__":
    main()