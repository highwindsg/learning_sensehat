from sense_hat import SenseHat
from time import sleep

sense = SenseHat()  # Assign the SenseHat() function to a variable sense.
sense.clear()       # From sense, get the attribute of the clear function.

pressure = sense.get_pressure()     # From the 'get_pressure()' function you obtain
                                    # the pressure readings from sense, and assign
                                    # the readings to variable pressure.
print(pressure)     # Then print what is being assigned to the pressure variable.
