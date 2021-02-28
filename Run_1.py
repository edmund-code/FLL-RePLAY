#!/usr/bin/env pybricks-micropython

import fll_briarcliff6pack
from pybricks.parameters import Stop
import time

my_robot = fll_briarcliff6pack.Bri6Pack()
drive_base = my_robot.drive_base

rotated = 0
my_robot.small_motor_left.reset_angle(angle=0)
fail_count = 0
while rotated <= 600:
        my.robot.small_motor_left.run_time(speed=500, time=500, then=Stop.HOLD, wait=False)
        rotated = my_robot.small_motor_left.angle()

        if my_robot.small_motor_left.control.stalled():
            # TODO: add a max counter to bail out
            print("stalled")
            print("rotated:" + str(rotated))
            if fail_count < 3:
                my_robot.small_motor_left.run_time(speed=-1000, time=500, then=Stop.COAST, wait=True)
            else:
                my_robot.small_motor_left.run_time(speed=-500, time=200, then=Stop.COAST, wait=True)
            rotated = my_robot.small_motor_left.angle()
            print("rotated:" + str(rotated))
            fail_count = fail_count + 1

    rotated = my_robot.small_motor_left.angle()
    print("final rotated:" + str(rotated))
    my_robot.small_motor_left.run_time(speed=-1000, time=600, then=Stop.COAST, wait=True)

    #reverse to mission 08
    drive_base.straight(-50)
    drive_base.turn(-15)
    drive_base.straight(-150)
    drive_base.turn(40)

    # lower the orange boom for mission 8
    while rotated > 340:
        my_robot.small_motor_left.run_time(speed=-1000, time=100, then=Stop.COAST, wait=True)
        rotated = my_robot.small_motor_left.angle()

    # GOTO mission 08
    drive_base.straight(220)

    # lift the orange boom
    while rotated < 650:
        my_robot.small_motor_left.run_time(speed=1000, time=100, then=Stop.COAST, wait=True)
        rotated = my_robot.small_motor_left.angle()

    # #TODO: turn and reverse to bench
    drive_base.turn(65)
    drive_base.stop()
    drive_base.settings(straight_acceleration=1000)
    drive_base.straight(-800)