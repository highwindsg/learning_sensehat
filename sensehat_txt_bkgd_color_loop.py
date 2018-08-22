from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)

# back_colour alters the colour of the background
# and works in the same way as text_colour.
# The while loop ensures the message shows continuously
# with a scrolling speed of 0.08.
# The default value is 0.1.
# The bigger the number, the slower the speed.
while True:
    sense.show_message("Sense Hat is awesome!", text_colour=yellow, back_colour=blue, scroll_speed=0.08)
    sleep(3)
#sense.clear()
