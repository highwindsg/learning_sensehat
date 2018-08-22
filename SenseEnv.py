from sense_hat import SenseHat
import time
from time import asctime    #to bring in the current time function

sense = SenseHat()  #establishing a communication between the Sense Hat
                    #and the porogram.

while True:
    #temp = round(sense.get_temperature()*1.8 +32)  # Round off temp to Fahrenheit as a integer.
    temp = int(sense.get_temperature())     # Obtain temperature reading as integer
    humidity = int(sense.get_humidity())    # Obtain humidity reading as integer
    pressure = int(sense.get_pressure())    # Obtain pressure reading as integer
    #message = " T = %ddeg, H = %d, P = %d " %(temp, humidity, pressure)
    message = " Temp: %s C, Humidity: %s rH, Pressure: %s Millibars " %(temp, humidity, pressure)
    #sense.show_message(message, scroll_speed = (0.08), text_colour = [200,240,200], back_colour = [0,0,0])
    time.sleep(4)
    log = open('weather.txt', "a")  # Opens a weather text file and append
    now = str(asctime())            # the current time and
    log.write(now+''+message+'\n')  # write in with the message of the T, H and P.
    print(message)  # At the same time, print out the message on screen.
    log.close()     # Then close the log file for this run cycle.
    time.sleep(5)   # Wait for 5 secs then restart the while loop again.
