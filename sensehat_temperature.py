from sense_hat import SenseHat
from time import sleep

sense = SenseHat()  # Assign the 'SenseHat()' function to the variable sense.
sense.clear()       # From sense, get the clear screen function.

temp = sense.get_temperature()  # Get the temperature reading from the
                                # 'get_temperature()' function from sense and
                                # assign it to the variable temp.
print(temp)         # Then print the temperature reading from the temp variable.
