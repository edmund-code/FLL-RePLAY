#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from pybricks.parameters import Direction 
from pybricks.robotics import DriveBase
import sys
import time
import fll_briarcliff6pack

# Initialize the EV3 Brick.
ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
small_motor_left = Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)

gyro_sensor = GyroSensor(Port.S3, Direction.CLOCKWISE)


# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=93.5, axle_track=120)

def Move_PID(distance): 

    gyro_sensor.reset_angle(0)

    err_p = 0.0
    err_i = 0.0
    err_d = 0.0

    err_prev = 0.0
    i = 0

    while robot.distance() <= distance:
    
            i += 1
            err_prev = err_p

   
            err_p = 0 - gyro_sensor.angle()
            err_i += err_p
            err_d = err_p - err_prev

            kp = 4
            ki = 0.02
            kd = 2

            if err_i >= 10000:
                err_i /= 2

            turn_rate = kp * err_p + ki * err_i + kd * err_d
            robot.drive(-200, -turn_rate)

            if (i % 20 == 0):
                print("Time={}, turn rate={}, P={}, I={}, D={}".format(i, turn_rate, err_p, err_i, err_d))
    
#Move_PID(100)
#robot.turn(90)
#Move_PID(-50)
#Move_PID(650)
#robot.turn(30)
#Move_PID(75)
#small_motor_left.run_angle(160, 650, wait=True)
#small_motor_left.run_angle(160, -100, wait=True)
#Move_PID(-600)


#robot.settings(200,200,60,60)
#robot.straight(-680)
#robot.turn(28)
#robot.straight(-180

small_motor_left.run_angle(200, 650, wait=True)
small_motor_left.run_angle(160, -650, wait=False)
robot.straight(500)
#Move_PID(1000)
