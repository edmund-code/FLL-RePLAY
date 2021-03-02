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
        # the sign of the input speed is ignored
        speed = abs(speed)

        # direction is indicated by the sign of the input distance  
        # postive distance ==> move forward
        # negative distance ==> move backward
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

        factor = abs(speed / 300.0) 
        deltaT = 0.1

        total_distance = abs(distance)
        gyro_PID_distance = total_distance / 2.0

        # use gyro_PID for the first half
        while abs(drive_base.distance()) <= gyro_PID_distance
            err_p = 0.0 - gyro_sensor.angle()
            err_i += err_p * deltaT
            err_d = (err_p - err_prev) / deltaT

            kp = 1 * factor
            ki = 1.5 * factor
            kd = 0.01 * factor

            # limit the speed err_i can grow (exponential decay)
            if abs(err_i) >= 100:
                err_i *= math.exp(-abs(err_i/100))

            turn_rate = kp * err_p + ki * err_i + kd * err_d 

            drive_base.drive(speed, turn_rate)

            time.sleep(deltaT)

            # debugging output 
            if (i % 1 == 0):
                print("Count={}, Distance={}, Angle={}, turn rate={}, P={}, I={}, D={}".format(i, drive_base.distance(), drive_base.angle(), turn_rate, err_p, err_i, err_d))

            i += 1
            err_prev = err_p

        # finish the distance with motor_PID
        motor_PID_distance = total_distance - abs(drive_base.distance())
        drive_base.stop()  
        drive_base.settings(straight_speed=speed)
        drive_base.straight(motor_PID_distance)
        
        print("Final: Distance={} gyroAngle={}".format(drive_base.distance(), gyro_sensor.angle()))
        

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