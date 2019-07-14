#!/usr/bin/env python3
from sense_hat import SenseHat
from time import sleep


sense = SenseHat()
sense.clear()

sense.set_pixel(2, 2, (0, 0, 255))
sense.set_pixel(4, 2, (0, 0, 255))
sense.set_pixel(3, 4, (100, 0, 0))
sense.set_pixel(1, 5, (255, 0, 0))
sense.set_pixel(2, 6, (255, 0, 0))
sense.set_pixel(3, 6, (255, 0, 0))
sense.set_pixel(4, 6, (255, 0, 0))
sense.set_pixel(5, 5, (255, 0, 0))

try:
    while True:
        sense.set_rotation(180)
        sleep(2)
        sense.flip_h()
        sleep(2)
        sense.flip_v()
        #sleep(2)
        #sense.clear()
        
except KeyboardInterrupt:
    pass

sense.clear()



