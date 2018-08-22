from sense_hat import SenseHat

sense = SenseHat()      # Set sense to an instance of the SenseHat function.
sense.scroll_speed = 0.9    # The default value is 0.1 if this line is not set.
                            # The bigger the number, the slower the speed.
sense.show_message("This is a test message.")
