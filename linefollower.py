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

#robot.straight(getDistance(50))
#robot.settings(straight_speed = 219, straight_acceleration = 876, turn_rate = 193, turn_acceleration = 773)

#robot.stop()
#wait(1000)

robot.settings(straight_speed = 250, straight_acceleration = 100, turn_rate = 200, turn_acceleration = 200)


# Calculate the light threshold. Choose values based on your measurements.
BLACK = 7
WHITE = 74
threshold = 25.0

# Set the gain of the proportional line controller. This means that for every
# percentage point of light deviating from the threshold, we set the turn
# rate of the drivebase to 1.2 degrees per second.

DRIVE_SPEED = -100

# For example, if the light value deviates from the threshold by 10, the robot
# steers at 10*1.2 = 12 degrees per second.
PROPORTIONAL_GAIN = 200
# Start following the line endlessly.

err_p = 0.0
err_i = 0.0
err_d = 0.0

err_prev = 0.0
i = 0

while True:
    i += 1
    err_prev = err_p

    # Calculate the deviation from the threshold.
    err_p = line_sensor.reflection() - threshold
    err_i += err_p
    err_d = err_p - err_prev

    kp = 3
    ki = 0.02
    kd = 0.4

    # Calculate the turn rate.
    turn_rate = kp * err_p + ki * err_i + kd * err_d

    # Set the drive base speed and turn rate.

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
    
    # You can wait for a short time or do other things in this loop.
  