# Briarcliff 6-Pack @ FLL RePLAY 2020-2021

You can use the [editor on GitHub](https://github.com/edmund-code/FLL-RePLAY/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

## Robot Game

## Research

## Core Values
### Discovery: We explore new skills and ideas.
### Innovation: We use creativity and persistence to solve problems.
### Impact:  We apply what we learn to improve our world.
### Inclusion: We respect each other and embrace our differences.
### Teamwork: We are stronger when we work together.
### Fun: We enjoy and celebrate what we do!


# Python 
[pybrick](https://pybricks.github.io/ev3-micropython/)
```
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S3)
```

```
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from pybricks.parameters import Direction
from pybricks.robotics import DriveBase
import sys
import time

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
small_motor_left = Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, 93.5, 120)

for i in range(3):
    small_motor_left.run_angle(-200, 550, wait=True)
    small_motor_left.hold()
    time.sleep(3)
    small_motor_left.run_angle(200, 550, wait=True)
```

[Link](url) and ![Image](src)
For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/edmund-code/FLL-RePLAY/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
