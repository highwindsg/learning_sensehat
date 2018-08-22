from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)

# back_colour alters the colour of the background
# and works in the same way as text_colour.
sense.show_message("Sense Hat is awesome!", text_colour=yellow, back_colour=blue)
sleep(2)
sense.clear()
