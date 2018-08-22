from sense_hat import SenseHat

sense = SenseHat()
r = 255     # r means red color
g = 255     # g means green color
b = 255     # b means blue coloe
            # Their values specify how bright each colour should be;
            # each value can be between 0 and 255.
            # The maximum value (255) has been used, hence is white.
            # You can change the value to show different color.

sense.clear((r, g, b))
