#!/usr/bin/env python3

from sense_hat import SenseHat
sense = SenseHat()


sense.clear()

blue = (0, 0, 255)
yellow = (255, 255, 0)

# We use the 'try' statement so that we can break out of the trigger.
try:
    sense.show_message("Astro Pi is awesome!", text_colour = yellow, back_colour = blue)

# And when the break out is done by a Ctrl+C, the 'try' looks for a 'KeyboardInterrupt'
# exception and ignores it. So that the script will exit cleanly by calling a 'pass'.
except KeyboardInterrupt:
    pass

