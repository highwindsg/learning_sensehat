from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Generate a random colour
def pick_random_colour():   # Define a function named pick_random_colour.
    random_red = randint(0, 255)    # Assign the variable random_red with a any
                                    # integer value from 0 up to 254.
    random_green = randint(0, 255)  # Assign the variable random_green with any
                                    # integer from 0 up to 254.
    random_blue = randint(0, 255)   # Assign the variable random_blue with a
                                    # any integer from 0 up to 254.
    return (random_red, random_green, random_blue)  # Get the random integer
                                                    # obtained from the three
                                                    # variables and return to the
                                                    # pick_random_colour function.

sense.show_letter("L", pick_random_colour())
sleep(1)
sense.show_letter("a", pick_random_colour())
sleep(1)
sense.show_letter("u", pick_random_colour())
sleep(1)
sense.show_letter("r", pick_random_colour())
sleep(1)
sense.show_letter("a", pick_random_colour())
sleep(1)

sense.clear()
