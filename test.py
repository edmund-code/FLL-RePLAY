#!/usr/bin/env pybricks-micropython

import fll_briarcliff6pack
from pybricks.parameters import Stop
import time

my_robot = fll_briarcliff6pack.Bri6Pack()
drive_base = my_robot.drive_base

# You can only change the settings while the robot is stopped. 
# This is either before you begin driving or after you call stop().

# for i in range(3):
#     my_robot.drive_pid(600, -1500)
#     time.sleep(1)
#     my_robot.drive_pid(600, 1500)
#     time.sleep(1)

# drive_base = my_robot.drive_base
# drive_base.settings(straight_speed=100, turn_rate=100)
# drive_base.turn(-90)


drive_base.settings(straight_speed=600)
for i in range(3):
    drive_base.straight(-1500)
    time.sleep(1)
    drive_base.straight(1500)
    time.sleep(1)