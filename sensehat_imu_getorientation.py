from sense_hat import SenseHat
sense = SenseHat()      # Assign variable sense with the SenseHat function.
sense.clear()           # From sense, get the clear function.

o = sense.get_orientation()     # Assign o with the get_orientation function from sense.
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]
print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
