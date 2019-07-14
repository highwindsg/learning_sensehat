#!/usr/bin/env python3
from sense_hat import SenseHat
from time import sleep


sense = SenseHat()
sense.clear()

# Define some colours
g = (0, 255, 0) # Green
b = (0, 0, 0) # Black

# Set up where each colour will display
creeper_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
]

try:
    while True:
        # Display these colours on the LED matrix
        sense.set_pixels(creeper_pixels)

except KeyboardInterrupt:
    pass

sense.clear()
