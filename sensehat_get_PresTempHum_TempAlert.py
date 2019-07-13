#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep


sense = SenseHat()
sense.clear()

# Define the colours red and green
red = (255, 0, 0)
green = (0, 255, 0)

pressure = sense.get_pressure()
pressure = round(pressure, 1) # Round off the pressure to 1 decimal place.
print("Pressure now is", pressure)

temp = sense.get_temperature()
temp = round(temp, 1) # Round off the temp to 1 decimal place.
print("Temperature now is", temp)

humidity = sense.get_humidity()
humidity = round(humidity, 1) # Round off humidity to 1 decimal place.
print("Humidity now is", humidity)

while True:
    message = "Temperature: " + str(temp) + " Pressure: " + str(pressure) + " Humidity: " + str(humidity)
    
    if temp > 18.3 and temp < 26.7:
        bg = green
    else:
        bg = red
        
    # From sense, use the show_message method to scroll the message at speed 0.1.
    sense.show_message(message, scroll_speed = 0.5, back_colour=bg)
