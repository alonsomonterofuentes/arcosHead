#!/usr/bin/python

"""
Servo.py
-------------

Controls a servo on a given channel by moving it to a position
between 0(0) and 1(180) using Adafruit's library for the PCA9685

"""

# Author: Alonso Montero <alon182@gmail.com
# License:  GPL v2

import Adafruit_PCA9685
from time import sleep
class Servo():

    def __init__(self, channel, frequency=240,
                 minPulseLength=150,
                 maxPulseLength=510,speed=1):
        self.channel = channel
        self.frequency = frequency
        self.minPulseLength = minPulseLength
        self.maxPulseLength = maxPulseLength
        self.speed = speed
        self.setup(frequency)

    def setup(self, frequency):
        """ Sets up the necesary information for the servo to work correectly
        """
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(frequency)

    def positionToPulse(self, position):
        """ Returns the given position (0 to 1) converted into
            a pulse length (minPulseLength to max pulse length)
        """
        return (position) * (self.maxPulseLength - self.minPulseLength) / 1 + self.minPulseLength
        
     

    def write(self, position):
        """Moves servo to required position
        """
        self.pwm.set_pwm(self.channel, 0, int(self.positionToPulse(position)))
        position = float(position)
        print "Moved Servo on channel " + str(self.channel) + " to position " + str(self.positionToPulse(position)) + "(" + str(position) + ")"
        sleep(self.speed)

