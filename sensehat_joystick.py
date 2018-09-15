# This code will print out the direction that the joystick is pushed in,
# or the direction from which it was released.
from sense_hat import SenseHat

sense = SenseHat()

while True:
    for event in sense.stick.get_events():  # From the stick attribute, use the
                                            # 'get_events()' function to obtain
                                            # the events.
        print(event.direction, event.action)    # Print out the direction and
                                                # action from event.
