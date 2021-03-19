#!/usr/bin/env pybricks-micropython
import fll_briarcliff6pack
my_robot = fll_briarcliff6pack.Bri6Pack()

import R1_basketball
my_robot.reset_motors()
my_robot.count_down(12)

import R2_bench
my_robot.reset_motors()
my_robot.count_down(12)

import R4_slide
my_robot.reset_motors()
my_robot.count_down(20)

import R5_final_run
my_robot.say("I will not fall")
my_robot.say("Briarcliff Six Pack Rocks")