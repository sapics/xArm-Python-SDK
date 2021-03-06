#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2019, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

"""
Move line(linear motion)
    1. explicit setting is_radian=True, set the default unit is radians
    set_position:
        1. explicit setting wait=True to wait for the arm to complete
"""

import os
import sys
import math
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI

arm = XArmAPI('192.168.1.113', is_radian=True)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

arm.reset(wait=True)

arm.set_position(x=300, y=0, z=150, roll=math.radians(180), pitch=0, yaw=0, speed=100, wait=True)
print(arm.get_position())
arm.set_position(x=300, y=200, z=250, roll=math.radians(180), pitch=0, yaw=0, speed=200, wait=True)
print(arm.get_position())
arm.set_position(x=500, y=200, z=150, roll=math.radians(180), pitch=0, yaw=0, speed=300, wait=True)
print(arm.get_position())
arm.set_position(x=500, y=-200, z=250, roll=math.radians(180), pitch=0, yaw=0, speed=400, wait=True)
print(arm.get_position())
arm.set_position(x=300, y=-200, z=150, roll=math.radians(180), pitch=0, yaw=0, speed=500, wait=True)
print(arm.get_position())
arm.set_position(x=300, y=0, z=250, roll=math.radians(180), pitch=0, yaw=0, speed=600, wait=True)
print(arm.get_position())

arm.disconnect()
