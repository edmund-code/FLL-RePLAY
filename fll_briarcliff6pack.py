#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from pybricks.parameters import Direction 
from pybricks.robotics import DriveBase
import sys
import time
import math

class Bri6Pack:
    def __init__(self):
        # Initialize the EV3 Brick.
        self.ev3 = EV3Brick()

        # large motors
        self.left_motor = Motor(Port.A)
        self.right_motor = Motor(Port.B)

        # small (medium) motors
        self.small_motor_left = Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)
        self.small_motor_right = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None)
        
        # gyro sensor
        self.gyro_sensor = GyroSensor(Port.S3, Direction.CLOCKWISE)

        # Initialize the drive base.
        self.drive_base = DriveBase(left_motor, right_motor, wheel_diameter=93.5, axle_track=120)
        return
    
    """
    A proportional–integral–derivative controller 
    """
    def Move_PID(speed, distance): 
        drive_base = self.drive_base
        gyro_sensor = self.gyro_sensor

        # reset gyro sensor
        gyro_sensor.reset_angle(0)

        err_p = 0.0
        err_i = 0.0
        err_d = 0.0

        err_prev = 0.0
        i = 0

        while drive_base.distance() <= distance:
                i += 1
                err_prev = err_p

                err_p = 0 - gyro_sensor.angle()
                err_i += err_p
                err_d = err_p - err_prev

                kp = 4
                ki = 0.02
                kd = 2

                # limit the speed err_i can grow (exponential decay)
                if abs(err_i) >= 100:
                    err_i *= math.exp(-abs(err_i))

                turn_rate = kp * err_p + ki * err_i + kd * err_d
                drive_base.drive(-speed, -turn_rate)

                if (i % 20 == 0):
                    print("Time={}, turn rate={}, P={}, I={}, D={}".format(i, turn_rate, err_p, err_i, err_d))
        
