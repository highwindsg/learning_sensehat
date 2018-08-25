from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# Define some colours
g = (0, 255, 0) # Green
b = (0, 0, 0)   # Black

# Set up where each colour will display
creeper_pixels = [
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g,
    g, g, g, g, g, g, g, g
]

# Display these colours on the LED matrix using the 'set_pixels' cmd to change
# all 64 LEDs using just one line of code.
sense.set_pixels(creeper_pixels)    # From sense get the set_pixels function and
                                    # set the creeper_pixels attribute.
sleep(5)
sense.set_rotation(180) # Rotate the display by 180 degrees.
sleep(5)
sense.flip_h()  # Flip the image on the screen horizontally.
#sleep(5)
#sense.flip_v() # Flip the image on the screen vertically.
sleep(5)
sense.clear()
