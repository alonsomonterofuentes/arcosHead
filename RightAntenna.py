

#!/usr/bin/python

"""
LeftAntenna.py
-------------
Controls the left antenna by moving it to a position
between 0(0) and 1(180) 

"""
# Author: Alonso Montero <alon182@gmail.com
# License:  GPL v2

from Servo import *
from conf import *

class LeftAntenna():
    def __init__(self)
        self.configuration = conf("Setting.ini")
        self.channel = self.configuration.get_setting("LeftAntenna","channel")
        self.frequency = self.configuration.get_setting("LeftAntenna","frequency")
        self.minPulseLength = self.configuration.get_setting("LeftAntenna","minPulseLength")
        self.maxPulseLength = self.configuration.get_setting("LeftAntenna","maxPulseLength")
        self.servo = Servo(self.channel, self.frequency, self.minPulseLength, self.maxPulseLength)
