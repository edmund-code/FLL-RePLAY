#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from pybricks.parameters import Direction
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
#small_motor = Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)

#gyro = GyroSensor(Port.S3)
#gyro.reset_angle(0)


# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=93.5, axle_track=120)

#small_motor.run_angle(200, 400)

#sys.exit()

# pid(kp, ki, kd, integral_range, integral_rate, feed_forward)
# default = (200, 600, 2, 18, 4, 0)
#print(robot.heading_control.pid())


robot.heading_control.pid(200, 600, 2, 180, 40, 0)

print(robot.heading_control.pid())

robot.settings(400)
robot.straight(-500)
robot.brake()
robot.settings(200)
robot.straight(500)
