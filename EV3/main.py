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
left_motor = Motor(Port.B)  # Change this to match.
right_motor = Motor(Port.C)  # Change this to match.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


def location(x, y):
    global robot_x
    global robot_y
    global direction
    # Calculating Turn
    atan_x = x - robot_x
    atan_y = y - robot_y
    turn = math.atan2(atan_y, atan_x)
    degrees = math.degrees(turn)
    direction = degrees
    robot.turn(degrees)
    print(degrees)  # Debugs how much it should turn by.
    print(direction)  # Debugs where it should be facing.
    distance = pow(pow(x - robot_x, 2) + pow(y - robot_y, 2), 0.5)
    print(distance)  # Debugs distance drove
    robot.straight(distance)
    robot_x = x
    robot_y = y

location(530, 460)
location(700 ,570)
location(700, 770)
location(760, 180)
