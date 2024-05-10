import math

robot_x = 0
robot_y = 0

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
    print(degrees)  # Debugs how much it should turn by.
    print(direction)  # Debugs where it should be facing.
    distance = pow(pow(x - robot_x, 2) + pow(y - robot_y, 2), 0.5)
    print(distance)  # Debugs distance drove
    robot_x = x
    robot_y = y

location(100, 0)
location(100, 100)
location(0, 100)
location(0, 0)