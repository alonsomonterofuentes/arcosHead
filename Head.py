"""
Head.py
-------------
Gets servo configuration from Setting.ini to correctly setup each servo on the head
"""
# Author: Alonso Montero <alon182@gmail.com
# License:  GPL v2

from Servo import Servo
from conf import conf

class Head(object):

    configuration = conf("Settings.ini")

    jaw = Servo(
        channel = int(configuration.get_setting("Jaw","channel")),
        frequency = int(configuration.get_setting("Jaw","frequency")),
        minPulseLength = int(configuration.get_setting("Jaw","minPulseLength")),
        maxPulseLength = int(configuration.get_setting("Jaw","maxPulseLength"))
    )

    left_antenna = Servo(
        channel = int(configuration.get_setting("LeftAntenna","channel")),
        frequency = int(configuration.get_setting("LeftAntenna","frequency")),
        minPulseLength = int(configuration.get_setting("LeftAntenna","minPulseLength")),
        maxPulseLength = int(configuration.get_setting("LeftAntenna","maxPulseLength"))
    )

    right_antenna = Servo(
        channel = int(configuration.get_setting("RightAntenna","channel")),
        frequency = int(configuration.get_setting("RightAntenna","frequency")),
        minPulseLength = int(configuration.get_setting("RightAntenna","minPulseLength")),
        maxPulseLength = int(configuration.get_setting("RightAntenna","maxPulseLength"))
    )

    left_brow_Vertical = Servo(
        channel = int(configuration.get_setting("LeftBrowVertical","channel")),
        frequency = int(configuration.get_setting("LeftBrowVertical","frequency")),
        minPulseLength = int(configuration.get_setting("LeftBrowVertical","minPulseLength")),
        maxPulseLength = int(configuration.get_setting("LeftBrowVertical","maxPulseLength"))
    )

    right_brow_vertical = Servo(
        channel = int(configuration.get_setting("RightBrowVertical","channel")),
        frequency = int(configuration.get_setting("RightBrowVertical","frequency")),
        minPulseLength = int(configuration.get_setting("RightBrowVertical","minPulseLength")),
        maxPulseLength = int(configuration.get_setting("RightBrowVertical","maxPulseLength"))
    )

    left_brow_horizontal = Servo(
        channel = int(configuration.get_setting("LeftBrowHorizontal","channel")),
        frequency = int(configuration.get_setting("LeftBrowHorizontal","frequency")),
        minPulseLength = int(configuration.get_setting("LeftBrowHorizontal","minPulseLength")),
        maxPulseLength = int(configuration.get_setting("LeftBrowHorizontal","maxPulseLength"))
    )

    right_brow_horizontal = Servo(
        channel = int(configuration.get_setting("RightBrowHorizontal","channel")),
        frequency = int(configuration.get_setting("RightBrowHorizontal","frequency")),
        minPulseLength = int(configuration.get_setting("RightBrowHorizontal","minPulseLength")),
        maxPulseLength = int(configuration.get_setting("RightBrowHorizontal","maxPulseLength"))
    )

    #import csv
    #f = open('happy.csv')
    #reader = csv.reader(f)
    #data = list(reader)
    #
    #def borrarColumna():
    #    for i in range(0,6):
    #        del data[i][0]
    #borrarColumna()
    #
    #for i in range(0,len(data[0])):
    #    print 1
    #    left_antenna.write((data[0][i]))

