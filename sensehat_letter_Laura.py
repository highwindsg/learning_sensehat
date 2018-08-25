from sense_hat import SenseHat  # To import the SenseHat function.
from time import sleep          # To import the sleep function.

sense = SenseHat()              # Assign the variable sense with the
                                # SenseHat function.

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

sense.show_letter("L", red)     # From sense get the show_letter function
                                # and to display L in red.
sleep(1)                        # To call the sleep function to pause for 1 sec.
sense.show_letter("a", blue)
sleep(1)
sense.show_letter("u", green)
sleep(1)
sense.show_letter("r", white)
sleep(1)
sense.show_letter("a", yellow)
sleep(1)
sense.clear()
