#!/usr/bin/env python3

"""
Create functions to fill the LED matrix with four different colours.
Add triggers to call one function for each possible direction in which the
joystick can be pressed.
"""

from sense_hat import SenseHat


sense = SenseHat()

# Define the functions.
def red():
    sense.clear(255, 0, 0) # From sense, use the clear method and set red color.

def blue():
    sense.clear(0, 0, 255) # From sense, use the clear method and set blue color.

def green():
    sense.clear(0, 255, 0) # From sense, use the clear method and set green color.

def yellow():
    sense.clear(255, 255, 0) # From sense, use the clear method and set yellow color.

# Tell the program to trigger which function to associate with which direction.

# From sense, get the stick attrib and for direction_up, set it to red.
sense.stick.direction_up = red
# From sense, get the stick attrib and for direction_up, set it to blue.
sense.stick.direction_down = blue
# From sense, get the stick attrib and for direction_left, set it to green.
sense.stick.direction_left = green
# From sense, get the stick attrib and for direction_right, set it to yellow.
sense.stick.direction_right = yellow
# From sense, get the stick attrib and for direction_middle, set it to clear all.
sense.stick.direction_middle = sense.clear

while True:
    pass # This keeps the program running to receive joystick events.
