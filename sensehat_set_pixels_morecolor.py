from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# Define some colours.
# Colour palette can obtain from https://www.w3schools.com/colors/colors_rgb.asp
B = (102, 51, 0)    # Dark brown colour.
b = (0, 0, 255)     # Blue colour.
S = (205, 133, 63)  # Light brown colour.
W = (255, 255, 255) # White colour.

# Set up where each colour will display
steve_pixels = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, S, S, S, S, S, S, B,
    S, S, S, S, S, S, S, S,
    S, W, b, S, S, b, W, S,
    S, S, S, B, B, S, S, S,
    S, S, B, S, S, B, S, S,
    S, S, B, B, B, B, S, S
]

# Display these colours on the LED matrix
sense.set_pixels(steve_pixels)  # From sense get the set_pixels attribute
                                # and set the steve_pixels params.
sleep(5)
sense.clear()
