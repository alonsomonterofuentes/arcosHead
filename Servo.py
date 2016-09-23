#!/usr/bin/python

"""
Servo.py
-------------

Controls a servo on a given channel by moving it to a position
between 0(0) and 1(180) using Adafruit's library for the PCA9685

TODO:
     *Check default values for frequency, min and max pulse
"""

# Author: Alonso Montero <alon182@gmail.com
# License:  GPL v2

import Adafruit_PCA9685


class Servo():

    def __init__(self, channel, frequency,
                 minPulseLength=150,
                 maxPulseLength=600):
        self.channel = channel
        self.minPulseLength = minPulseLength
        self.maxPulseLength = maxPulseLength
        setup(frequency, minPulseLength, maxPulseLength)

    def setup(self, frequency):
        """ Sets up the necesary information for the servo to work correectly
        """
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(frequency)

    def positionToPulse(self, position):
        """ Returns the given position (0 to 1) converted into
            a pulse length (minPulseLength to max pulse length)
        """
       return (position) * (maxPulseLength - minPulseLength) / 1 + minPulseLength
        
     
    def write(self,positions):
        """ Converts the given position to a pulse and then moves the servo there
        """
        for position in positions:
            pwm.set_pwm(self.channel, 0, positionToPulse(position))
            print "Moved Servo on channel " + str(self.channel) +
            " to " + str(positionToPulse(position)*180.0) + " degrees"
           
