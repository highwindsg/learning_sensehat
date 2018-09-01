from sense_hat import SenseHat
import time

sense = SenseHat()  # Assign the 'SenseHat()' function go the variable of sense.
sense.clear()       # From sense, get the 'clear()' function to clear any prior display.

# Get the pressure reading using the 'get_pressure()' function from sense.
P = sense.get_pressure()
# Get the temperature reading using the 'get_temperature()' function from sense.
T = sense.get_temperature()
# Get the humidity reading using the 'get_humidity()' function from sense.
H = sense.get_humidity()

# Obtain the readings of pressure(P), temperature(T) and humidity(H),
# round them to the nearest 1 decimal place, and assign to the message variable.
message = "Pressure: %s, Temperature: %s, Humidity: %s" %(round(P, 1), round(T, 1), round(H, 1))

# From sense, use the 'show_message()' function to scroll the message content
# at a speed of 0.08th of a sec.
sense.show_message(message, scroll_speed = (0.08))
