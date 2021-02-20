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

robot.settings(straight_speed=100, turn_rate=50)
robot.straight(-350) 
robot.turn(11)
robot.straight(-80)
robot.straight(20)
robot.turn(-15)
robot.stop()
robot.settings(straight_speed=500)
robot.straight(-100)
robot.straight(500)