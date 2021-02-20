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

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
small_motor_left = Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)

gyro_sensor = GyroSensor(Port.S3, Direction.CLOCKWISE)


# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=93.5, axle_track=120)

robot.settings(straight_speed=200)
robot.straight(-600)
robot.straight(600)