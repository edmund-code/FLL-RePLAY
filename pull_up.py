#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from pybricks.parameters import Direction
from pybricks.robotics import DriveBase
import sys
import time

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
small_motor_left = Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, 93.5, 120)

for i in range(3):
    small_motor_left.run_angle(-200, 550, wait=True)
    small_motor_left.hold()
    time.sleep(3)
    small_motor_left.run_angle(200, 550, wait=True)

