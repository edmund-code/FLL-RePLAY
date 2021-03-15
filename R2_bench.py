#!/usr/bin/env pybricks-micropython

import fll_briarcliff6pack
import sys
import time

# Initialize the drive base.
my_robot = fll_briarcliff6pack.Bri6Pack()
drive_base = my_robot.drive_base

drive_base.settings(straight_speed=250, turn_rate=50)
drive_base.straight(400) 
time.sleep(0.5)
drive_base.stop()
drive_base.settings(straight_speed=500, turn_rate=50)
drive_base.straight(120)
drive_base.straight(-500)
