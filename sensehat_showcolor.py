from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
#r = 255     # r means red color
#g = 255     # g means green color
#b = 255     # b means blue coloe
            # Their values specify how bright each colour should be;
            # each value can be between 0 and 255.
            # The maximum value (255) has been used, hence is white.
            # You can change the value to show different color.

# If uncomment line 5 to 7 and then comment out all of below,
# then will only show white color.
# Below lines shows white, red, green and blue after 2 sec sleep/pause.
rgb = (255, 255, 255)
sense.clear()
sleep(1)
sense.clear(rgb)
sleep(1)

red = (255,0 ,0)
sense.clear()
sleep(1)
sense.clear(red)
sleep(1)

green = (0, 255, 0)
sense.clear()
sleep(1)
sense.clear(green)
sleep(1)

blue = (0, 0, 255)
sense.clear()
sleep(1)
sense.clear(blue)
sleep(1)

sense.clear()
