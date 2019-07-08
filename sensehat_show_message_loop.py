#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)

while True:
    sense.show_message("Astro Pi is awesome!", text_colour = yellow, back_colour = blue)
    sleep(5)
