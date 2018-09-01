from sense_hat import SenseHat

sense = SenseHat()  # Assign the 'SenseHat()' function to a variable of sense.
sense.clear()       # Clear the screen using the 'clear()' function from sense.

humidity = sense.get_humidity()     # Get the humidity reading from sense and
                                    # assign it to the variable humidity.
print(humidity)     # Then print the humidity reading from the variable humidity.
