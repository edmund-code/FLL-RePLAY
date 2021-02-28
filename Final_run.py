#!/usr/bin/env pybricks-micropython

import fll_briarcliff6pack
from pybricks.parameters import Stop
import time

my_robot = fll_briarcliff6pack.Bri6Pack()
drive_base = my_robot.drive_base

# You can only change the settings while the robot is stopped. 
# This is either before you begin driving or after you call stop().

run_m02 = True
run_m08 = False
run_m06 = False

#set up hugging the wall and on the second line back

# M02 Step Counter
if run_m02:
    drive_base.settings(straight_speed=200)
    my_robot.drive_pid(speed=200, distance=630)
    drive_base.stop()
    drive_base.settings(straight_speed=14)
    drive_base.straight(220)
    drive_base.stop()

    # turn counter clockwise and prepare to go through the gate
    drive_base.settings(straight_speed=100, turn_rate=100)
    drive_base.straight(-90)
    drive_base.turn(-130)
    drive_base.straight(25)
    drive_base.turn(-16)
    drive_base.straight(-150)    # move backward to align with the wall
    my_robot.drive_pid(speed=200, distance=785)   # go through the gate
    drive_base.stop()

# M08 Boccia
if run_m08:
    drive_base.settings(straight_speed=30, turn_rate=30)
    drive_base.straight(-50)
    drive_base.turn(37)
    drive_base.stop()
    drive_base.settings(straight_speed=100, turn_rate=100)
    drive_base.straight(125)
    drive_base.straight(-40)
    drive_base.stop()
    drive_base.settings(straight_speed=30, turn_rate=30)
    drive_base.turn(-50)
    drive_base.straight(100)
    my_robot.small_motor_left.run_angle(-50, -40)   # dump the cubes
    drive_base.stop()

# M06 Pull-up Bar
if run_m06:
    my_robot.small_motor_right.run_angle(400, 900, wait=False)
    drive_base.settings(straight_speed=100, turn_rate=100)
    drive_base.straight(-390)
    my_robot.small_motor_right.run_angle(-400, 500, then=Stop.HOLD, wait=True)
    my_robot.small_motor_right.hold()


#drive_base.settings(straight_speed=100, turn_rate=100)
#drive_base.straight(100)

# my_robot.drive_pid(200, 400)
# drive_base.stop()
# time.sleep(2)
# my_robot.drive_pid(200, -400)

# drive_base.straight(400)
# drive_base.stop()
# time.sleep(5)
# drive_base.straight(-400)

#my_robot.drive_pid(10000, 1000)