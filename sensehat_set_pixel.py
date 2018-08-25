from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

blue = (0, 0, 255)
red = (255, 0, 0)

# From sense, get the set_pixel attribute and set params 0 on x-axis,
# 2 on y-axis with blue colour.
# The set_pixel cmd sets the LED pixel one at a time.
sense.set_pixel(0, 2, blue) # 0 is the top-left 1st LED on the x-axis
                            # just below the GPIO.
                            # 2 is the 3rd LED on the y-axis down from 0.
# From sense, get the set_pixel attribute and set params 7 on x-axis,
# 4 on y-axis with red colour.
sense.set_pixel(7, 4, red)  # 7 is the 8th LED on the x-axis. 4 is the 5th LED
                            # on the y-axis down.
sleep(5)
sense.clear()
