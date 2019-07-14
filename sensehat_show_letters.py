#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep


sense = SenseHat()
sense.clear()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

try:
    while True:
        sense.show_letter("M", red)
        sleep(1)
        sense.show_letter("a", blue)
        sleep(1)
        sense.show_letter("r", green)
        sleep(1)
        sense.show_letter("y", yellow)
        sleep(1)
        sense.clear()
        sleep(5)

except KeyboardInterrupt:
    pass

sense.clear()

    
