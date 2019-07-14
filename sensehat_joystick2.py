#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep


sense = SenseHat()

e = (0, 0, 0) # Empty color
w = (255, 255, 255) # While color

sense.clear() # Clear all previous output.

try:
    while True:
        for event in sense.stick.get_events():
            if event.action == "pressed":
            
                # Check which direction it was pressed.
                if event.direction == "up":
                    sense.show_letter("U") # Up arrow
                elif event.direction == "down":
                    sense.show_letter("D") # Down arrow
                elif event.direction == "left":
                    sense.show_letter("L")
                elif event.direction == "right":
                    sense.show_letter("R")
                elif event.direction == "middle":
                    sense.show_letter("M")
            
                sleep(0.5)
                sense.clear()

except KeyboardInterrupt:
    pass

sense.clear()

            