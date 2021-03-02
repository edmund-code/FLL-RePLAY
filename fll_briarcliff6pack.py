#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from pybricks.parameters import Direction
from pybricks.parameters import Stop
from pybricks.robotics import DriveBase
import sys
import time
import math

class Bri6Pack:
    def __init__(self):
        # Initialize the EV3 Brick.
        self.ev3 = EV3Brick()

        # large motors
        left_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE, gears=None)
        right_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears=None)

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
    def drive_pid(self, speed, distance): 
        # speed is always positive
        # postive distance ==> move forward
        # negative distance ==> move backward
        speed = abs(speed)
        if (distance < 0):
            speed = -speed
            distance = -distance

        drive_base = self.drive_base
        gyro_sensor = self.gyro_sensor

        # resets the estimated driven distance and angle to 0
        drive_base.reset()

        # reset gyro sensor
        gyro_sensor.reset_angle(0)

        err_p = 0.0
        err_i = 0.0
        err_d = 0.0

        err_prev = 0.0
        i = 0

        while abs(drive_base.distance()) <= abs(distance):
            i += 1
            err_prev = err_p

            err_p = 0.0 - gyro_sensor.angle() * 1.0
            err_i += err_p
            err_d = err_p - err_prev

            kp = 0.8
            ki = 0.002
            kd = 2

            # limit the speed err_i can grow (exponential decay)
            if abs(err_i) >= 100:
                err_i *= math.exp(-abs(err_i/100))

            turn_rate = kp * err_p + ki * err_i + kd * err_d
            drive_base.drive(speed, turn_rate)

            time.sleep(0.01)

            if (i % 20 == 0):
                print("Count={}, Distance={} turn rate={}, P={}, I={}, D={}".format(i, drive_base.distance(), turn_rate, err_p, err_i, err_d))

        drive_base.stop()  
        print("Count={}, Distance={} turn rate={}, P={}, I={}, D={}".format(i, drive_base.distance(), turn_rate, err_p, err_i, err_d))
        

    ## stall_tolerances(speed, time)
    ## If the controller cannot reach this "speed" 
    ## for some "time" even with maximum "actuation", it is stalled.
    # robot.distance_control.stall_tolerances(speed, 100)
    # robot.distance_control.limits(actuation = 40)
    
    def check_stall(self):
        if self.drive_base.distance_control.stalled():
            print("STALLED")
            self.drive_base.stop()
            return True