import math
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

# y = b - mx
# b = yint, x = i, m = b/x = yint/i

led_pin = board.D0
trig = DigitalInOut(board.D1)
trig.direction = Direction.INPUT
trig.pull = Pull.DOWN

num_pixels = 36

xint = 40
counter = 0
inc = 2
dec = 1

# ORANGE = (255, 37, 0)
r = 255
g = 37
b = 0

pixels = neopixel.NeoPixel(led_pin, num_pixels, brightness=1, auto_write=False)

def line(yint):
    for i in range(num_pixels):
        m = yint / xint
        coef = (yint - (m * i))/255
        red = r * coef
        green = g * coef
        blue = b * coef
        pixels[i] = (math.floor(red), math.floor(green), math.floor(blue))
        pixels.show()

while True:
    if trig.value:
        counter = counter + inc
        # time.sleep(0.05)
    else:
        counter = counter - dec
        # time.sleep(0.05)

    if counter < 0:
        counter = 0

    print(counter)

    if counter > 10:
        if counter > 256:
            counter = 256

        if counter < 255:
            line(counter-10)
        else:
            line(255)

    else:
        line(0)


    time.sleep(0.05)