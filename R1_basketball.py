#!/usr/bin/env pybricks-micropython
import fll_briarcliff6pack
from pybricks.parameters import Stop
import time
from pybricks.ev3devices import (ColorSensor)
from pybricks.parameters import Port, Color
my_robot = fll_briarcliff6pack.Bri6Pack()
drive_base = my_robot.drive_base
# Initialize the color sensor.
line_sensor1 = ColorSensor(Port.S1)
line_sensor2 = ColorSensor(Port.S2)
drive_base.settings(straight_acceleration=400, turn_acceleration=200)
drive_base.straight(-5)
# drive_base.straight(840)
my_robot.drive_pid(speed=300, distance=840)
# drive_base.stop()
# drive_base.settings(straight_speed=230)
# drive_base.straight(140)
# drive_base.turn(15)
# drive_base.straight(120)
# drive_base.turn(-22)
# # drive_base.stop()
# # drive_base.settings(straight_acceleration=100, turn_acceleration=200)
# drive_base.straight(230)
drive_base.straight(-15)
my_robot.small_motor_left.control.stall_tolerances(speed=15, time=1000)
# drive_base.stop()
# drive_base.settings(straight_acceleration=400, turn_acceleration=200)
rotated = 0
my_robot.small_motor_left.reset_angle(angle=0)
fail_count = 0
while rotated <= 600:
    my_robot.small_motor_left.run_time(speed=500, time=500, then=Stop.HOLD, wait=False)
    rotated = my_robot.small_motor_left.angle()
    if my_robot.small_motor_left.control.stalled():
        # TODO: add a max counter to bail out
        print("stalled")
        print("rotated:" + str(rotated))
        if fail_count < 10:
            my_robot.small_motor_left.run_time(speed=-1000, time=500, then=Stop.COAST, wait=True)
        else:
            my_robot.small_motor_left.run_time(speed=-500, time=200, then=Stop.COAST, wait=True)
        rotated = my_robot.small_motor_left.angle()
        print("rotated:" + str(rotated))
        fail_count = fail_count + 1
rotated = my_robot.small_motor_left.angle()
print("final rotated:" + str(rotated))
#lower boom
my_robot.small_motor_left.run_time(speed=-1000, time=600, then=Stop.COAST, wait=False)
#reverse to mission 08
drive_base.straight(-50)
drive_base.turn(-15)
drive_base.straight(-150)
drive_base.turn(41)
#drive_base.straight(-100)
#drive_base.turn(40)
# lower the orange boom for mission 8
my_robot.small_motor_left.run_time(speed=-1000, time=500, then=Stop.COAST, wait=False)
# GOTO mission 08
drive_base.straight(200)
# lift the orange boom
my_robot.small_motor_left.run_time(speed=1000, time=600, then=Stop.COAST, wait=True)
# turn and reverse to bench
# drive_base.turn(72)
# drive_base.stop()
# reflection1 = line_sensor1.reflection()
# reflection2 = line_sensor2.reflection()
# print("reflection1:"+str(reflection1))
# print("reflection2:"+str(reflection2))
# while reflection1 > 10:
#     drive_base.straight(10)
#     reflection1 = line_sensor1.reflection()
#     reflection2 = line_sensor2.reflection()
#     print("reflection1:"+str(reflection1))
#     print("reflection2:"+str(reflection2))
# while reflection2 >10:
#     drive_base.turn(1)
#     reflection2 = line_sensor2.reflection()
# #TODO: figure out what angle to turn
# drive_base.stop()
# drive_base.settings(straight_acceleration=400, turn_acceleration=200)
# drive_base.turn(-2.5)
drive_base.stop()
drive_base.settings(straight_speed=100000, straight_acceleration=1000)
drive_base.straight(-900)