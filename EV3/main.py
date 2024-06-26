#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
import math

robot_x = 0
robot_y = 0
direction = 0

# Initialization
ev3 = EV3Brick() 
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


# This function essentially just gets two coordinates, then makes the robot turn and drive to those coordinates
def location(x, y):
    global robot_x
    global robot_y
    global direction
    # Calculating Turn
    atan_x = x - robot_x
    atan_y = y - robot_y
    turn = math.atan2(atan_y, atan_x)
    degrees = math.degrees(turn)
    tempdirection = degrees
    degrees -= direction
    if (degrees < 0):
        degrees += 360
    if (tempdirection < 0):
        tempdirection += 360
    direction = tempdirection
    #degrees = abs(degrees)
    print(degrees)  # Debugs how much it should turn by.
    print(direction)  # Debugs where it should be facing.
    robot.turn(degrees)
    distance = pow(pow(x - robot_x, 2) + pow(y - robot_y, 2), 0.5)
    print(distance)  # Debugs distance drove
    robot.straight(distance)
    robot_x = x
    robot_y = y

# Actual Positions
location(530, 460)
location(700 ,570)
location(700, 770)
location(760, 180)