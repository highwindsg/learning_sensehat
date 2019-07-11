#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
pressure = round(pressure, 1)
print("Pressure now is", pressure)

temp = sense.get_temperature()
temp = round(temp, 1)
print("Temperature now is", temp)

humidity = sense.get_humidity()
humidity = round(humidity, 1)
print("Humidity now is", humidity)
