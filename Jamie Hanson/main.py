from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

ev3.speaker.beep()

#Left_Motor = Motor(Port.B)
#Right_Motor = Motor(Port.C)

#def BothMotor(x):
#    Left_Motor.run_target(500, 90)
#    Right_Motor.run_target(500, 90)