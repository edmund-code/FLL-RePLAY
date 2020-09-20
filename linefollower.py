#!/usr/bin/env pybricks-micropython
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.media.ev3dev import Font
import math

import sys
from sys import stderr

# Create your objects here.
ev3 = EV3Brick()

def getDistance(distance):
    return distance * -1

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S1)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=93.5, axle_track=120)

# settings
ev3.screen.clear()
ev3.screen.set_font(Font(size=9))
ev3.screen.print(robot.settings())
print(robot.settings(), file=stderr)

# Calculate the light threshold. Choose values based on your color sensor measurements.
BLACK = 7
WHITE = 74
threshold = 25.0

#reset PID controller
err_p = 0.0
err_i = 0.0
err_d = 0.0

err_prev = 0.0
i = 0

# Start following the line endlessly.
while True:
    i += 1
    err_prev = err_p

   
    err_p = line_sensor.reflection() - threshold
    err_i += err_p
    err_d = err_p - err_prev

    kp = 3
    ki = 0.02
    kd = 0.4


    turn_rate = kp * err_p + ki * err_i + kd * err_d


#set drive speed based on turn rate
    if (abs(turn_rate) > 40):
        DRIVE_SPEED = -10
        wait(3)
    elif (abs(turn_rate) > 80):
        DRIVE_SPEED = -5
        wait(1)
    else:
        DRIVE_SPEED = -100  # mm/sec
        wait(5)    # ms

    if (abs(turn_rate) > 30):
        err_i *= 0.5
        turn_rate *= 0.5

    if (i % 20 == 0):
        print("Time={}, turn rate={}, P={}, I={}, D={}".format(i, turn_rate, err_p, err_i, err_d))
    robot.drive(DRIVE_SPEED, turn_rate)
    

  