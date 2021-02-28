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

# M12 Row Machine
if run_m12:
    drive_base.settings(straight_speed=100, turn_rate=100)
    drive_base.turn(-20)
    drive_base.straight(95)
    my_robot.small_motor_left.run_angle(200, 350)  
    drive_base.straight(-75)

    drive_base.stop()
    drive_base.settings(straight_speed=100, turn_rate=50)
    drive_base.turn(-30)
    drive_base.turn(5)
    my_robot.small_motor_left.run_angle(200, -80)   # lift the arm
    drive_base.turn(-55)
    drive_base.straight(200)
    drive_base.turn(42)
#    my_robot.small_motor_left.run_angle(-150, -109)  
#    my_robot.small_motor_left.run_angle(-155, 130)

# M13 Weight Machine
if run_m13:
    drive_base.stop()
    drive_base.settings(straight_speed=100, turn_rate=100)
    my_robot.small_motor_left.run_angle(200, 40, wait=False)   # lower the arm
    drive_base.straight(408)
    
    my_robot.small_motor_left.run_angle(80, -250) # raise the arm
    my_robot.small_motor_left.run_angle(100, 100)
    drive_base.straight(-70)
    
    my_robot.small_motor_left.run_angle(100, -160) # reset arm to the original height