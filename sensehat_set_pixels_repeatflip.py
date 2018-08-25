from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)

image = [
e, w, w, e, e, w, w, e,
w, e, e, e, e, e, e, w,
w, w, w, e, e, w, w, w,
w, w, b, e, e, w, w, b,
w, w, w, e, e, w, w, w,
e, e, e, e, e, e, e, e,
e, e, w, w, w, w, e, e,
e, w, e, e, e, e, w, e
]

sense.set_pixels(image)

while True:
    sleep(1)
    sense.flip_h()  # Therefore the blue eyeball will flip horizontally,
                    # thus giving the visual that it is looking from right
                    # to left repeatly every second.
