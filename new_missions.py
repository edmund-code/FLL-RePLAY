#!/usr/bin/env pybricks-micropython

import fll_briarcliff6pack
from pybricks.parameters import Stop
import time

my_robot = fll_briarcliff6pack.Bri6Pack()
drive_base = my_robot.drive_base

# You can only change the settings while the robot is stopped. 
# This is either before you begin driving or after you call stop().

run_m12 = True
run_m13 = True

my_robot.drive_pid(500, 1500)
my_robot.drive_pid(250, 250)
time.sleep(1)
my_robot.drive_pid(70, -270)

# M12 Row Machine
if run_m12:
    drive_base.settings(straight_speed=100, turn_rate=100)
    drive_base.turn(-40)
    drive_base.straight(60)
    my_robot.small_motor_left.run_angle(200, 350)  
    drive_base.straight(-70)

    drive_base.stop()
    drive_base.settings(straight_speed=100, turn_rate=50)
    drive_base.turn(-40)
    drive_base.turn(5)
    drive_base.straight(30)
    my_robot.small_motor_left.run_angle(200, -100)   # lift the arm
    drive_base.turn(-33)
    drive_base.straight(200)
    drive_base.turn(52)
#    my_robot.small_motor_left.run_angle(-150, -109)  
#    my_robot.small_motor_left.run_angle(-155, 130)

# M13 Weight Machine
if run_m13:
    drive_base.stop()
    drive_base.settings(straight_speed=100, turn_rate=100)
    my_robot.small_motor_left.run_angle(200, 75, wait=False)   # lower the arm
    drive_base.straight(355)
    
    my_robot.small_motor_left.run_angle(80, -250) # raise the arm
    my_robot.small_motor_left.run_angle(100, 100)
    drive_base.straight(-70)
    
    my_robot.small_motor_left.run_angle(100, -160) # reset arm to the original height