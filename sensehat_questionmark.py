from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

X = [255, 0, 0]     # Red
O = [255, 255, 255]     # White

question_mark = [   # Marks the spot in the list where there is red or white color.
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)     # To set the pixels with above marked spots.
sleep(5)    # Let the display show for 5 secs.
sense.clear()   # Then clears the display.
