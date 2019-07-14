#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

blue = (0, 0, 255)
yellow = (255, 255, 0)

try:
    while True:
        sense.show_message("Astro Pi is awesome!", text_colour = yellow, back_colour = blue)
        sleep(5)

except KeyboardInterrupt:
    pass

sense.clear() # To clear the LED matrix display even after a interrupted sequence.

