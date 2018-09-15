from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration["x"]
    y = acceleration["y"]
    z = acceleration["z"]

    # The abs() function is not specific to Sense Hat library,
    # instead it is part of standard Python.
    # abs() gives us the absolute of a value and ignore whether the actual
    # value is positive or negative. eg. abs(1) and abs(-1) both return 1.
    # This function is helpful because we don't care in which direction
    # the sensor is being shaken, just that it is shaken.
    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
        sense.show_letter("!", red)     # We show a exclamation mark instead of
                                        # a actual alphabet letter.
    else:
        sense.clear()
