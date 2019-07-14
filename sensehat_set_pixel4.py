#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep


sense = SenseHat()
sense.clear()

w = (150, 150, 150)    # w means white
b = (0, 0, 255)        # b means blue
e = (0, 0, 0)          # e means empty

image = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    w,w,w,e,e,w,w,w,
    w,w,b,e,e,w,w,b,
    w,w,w,e,e,w,w,w,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

try:
    sense.set_pixels(image)

    while True:
        sleep(1)
        sense.flip_h()
        
except KeyboardInterrupt:
    pass

sense.clear()

