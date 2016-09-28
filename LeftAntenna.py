
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
        self.channel = self.configuration.getSetting("LeftAntenna","channel")
        self.frequency = self.configuration.getSetting("LeftAntenna","frequency")
        self.minPulseLength = self.configuration.getSetting("LeftAntenna","minPulseLength")
        self.maxPulseLength = self.configuration.getSetting("LeftAntenna","maxPulseLength")
        self.servo = Servo(self.channel, self.frequency, self.minPulseLength, self.maxPulseLength)

    def move(positions):
        self.servo.move(positions)

