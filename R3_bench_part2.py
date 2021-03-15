#!/usr/bin/env pybricks-micropython

import fll_briarcliff6pack
from pybricks.parameters import Stop
import sys
import time

# Initialize the drive base.
my_robot = fll_briarcliff6pack.Bri6Pack()
drive_base = my_robot.drive_base

my_robot.drive_pid(speed=150, distance=600) 
my_robot.drive_pid(speed=150, distance=-600) 

