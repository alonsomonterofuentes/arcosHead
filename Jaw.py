#!/usr/bin/python

"""
LeftAntenna.py
-------------
Controls the jaw by moving it to a position
between 0(closed) and 1(open) 
Gets setup configuration from 
"""
# Author: Alonso Montero <alon182@gmail.com
# License:  GPL v2

from Servo import *
from conf import conf

class LeftAntenna():
    def __init__(self)
        self.configuration = conf("Setting.ini")
        self.channel = self.configuration.get_setting("Jaw","channel")
        self.frequency = self.configuration.get_setting("Jaw","frequency")
        self.minPulseLength = self.configuration.get_setting("Jaw","minPulseLength")
        self.maxPulseLength = self.configuration.get_setting("Jaw","maxPulseLength")
        self.servo = Servo(self.channel, self.frequency, self.minPulseLength, self.maxPulseLength)
