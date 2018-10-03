from sense_hat import SenseHat
import time
from time import asctime    # To bring in the current time function.

sense = SenseHat()          # Assigning var sense with the SenseHat function.

#red = (255, 0, 0)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration["x"]
    y = acceleration["y"]
    z = acceleration["z"]

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
#        sense.show_letter("!", red)
        message = " This chair is occupied. "
        log = open('chair.txt', "a")    # Open the file in appending mode.
        now = str(asctime())
        log.write(now + '' + message + '\n' )   # Starts writing current date
                                                # and time with the message.
        print(message)      # Optional. Prints output to console screen.
        log.close()         # Close the log file.
        time.sleep(5)      # Wait for 5 secs before running loop again.
#    else:
#        sense.clear()
