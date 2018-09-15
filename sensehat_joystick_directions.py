# Depending on which way the joystick was pressed,
# display one of the letters U, D, L, R or M on the LED matrix.

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

e = (0, 0, 0)           # optional
w = (255, 255, 255)     # optional

sense.clear()
while True:
    for event in sense.stick.get_events():
        # Check if the joystick was presses
        if event.action == "pressed":

        # Check which direction
            if event.direction == "up":
                sense.show_letter("U")      # Up arrow
            elif event.direction == "down":
                sense.show_letter("D")
            elif event.direction == "left":
                sense.show_letter("L")
            elif event.direction == "right":
                sense.show_letter("R")
            elif event.direction == "middle":
                sense.show_letter("M")

            # Wait a while and then clear the screen.
            sleep(0.5)
            sense.clear()
