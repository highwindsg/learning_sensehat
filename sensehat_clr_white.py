from sense_hat import SenseHat  # From sense_hat import the SenseHat function.

sense = SenseHat()  # Assign the variable sense with the SenseHat function.

r = 255
g = 255
b = 255

sense.clear((r, g, b))  # Instead of clearing the screen, fill in the clear
                        # attribute with colour r, g, b.
