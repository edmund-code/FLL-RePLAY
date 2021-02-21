#!/usr/bin/env pybricks-micropython

import fll_briarcliff6pack
from pybricks.parameters import Stop
import sys
import time

# Initialize the drive base.
my_robot = fll_briarcliff6pack.Bri6Pack()
drive_base = my_robot.drive_base

drive_base.settings(straight_speed=100, turn_rate=50)
drive_base.straight(350) 
drive_base.turn(11)
drive_base.straight(80)
drive_base.straight(-20)
drive_base.turn(-15)
drive_base.stop()
drive_base.settings(straight_speed=500)
drive_base.straight(100)
drive_base.straight(-500)