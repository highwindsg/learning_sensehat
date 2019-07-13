#!/usr/bin/env python3

from sense_hat import SenseHat
sense = SenseHat()


while True:
    for event in sense.stick.get_events(): # From sense, get the stick attrib
                                           # and use the get_events method.
        print(event.direction, event.action) # Print out the direction of the
                                             # event, and the action of the event.
        