"""Example to cycle a bulb between colors in a list, with a smooth fade between.
Assumes the bulb is already on.
The python file with the Flux LED wrapper classes should live in
the same folder as this script
"""
from itertools import cycle
import os
import sys
import time
from medianColour import find_median_colour
from screenshot import screenshot
from flux_led import BulbScanner, WifiLedBulb

this_folder = os.path.dirname(os.path.realpath(__file__))
sys.path.append(this_folder)


def crossFade(bulb, color1, color2):

    r1, g1, b1 = color1
    r2, g2, b2 = color2

    steps = 100
    for i in range(1, steps + 1):
        r = r1 - int(i * float(r1 - r2) / steps)
        g = g1 - int(i * float(g1 - g2) / steps)
        b = b1 - int(i * float(b1 - b2) / steps)
        # (use non-persistent mode to help preserve flash)
        bulb.setRgb(r, g, b, persist=False)


def main():

    # Find the bulb on the LAN
    scanner = BulbScanner()
    scanner.scan(timeout=4)

    # Specific ID/MAC of the bulb to set
    bulb_info = scanner.getBulbInfoByID("ACCF235FFFFF")

    if bulb_info:

        bulb = WifiLedBulb(bulb_info["ipaddr"])

        color_time = 1.5  # seconds on each color
        imagePath = 'image1.png' #which image is being used

        red = (255, 0, 0)
        orange = (255, 125, 0)
        yellow = (255, 255, 0)
        springgreen = (125, 255, 0)
        green = (0, 255, 0)
        turquoise = (0, 255, 125)
        cyan = (0, 255, 255)
        ocean = (0, 125, 255)
        blue = (0, 0, 255)
        violet = (125, 0, 255)
        magenta = (255, 0, 255)
        raspberry = (255, 0, 125)
        colorwheel = [
            red,
            orange,
            yellow,
            springgreen,
            green,
            turquoise,
            cyan,
            ocean,
            blue,
            violet,
            magenta,
            raspberry,
        ]

        while True:

            screenshot()

            bulb.refreshState()

            averageColour = find_median_colour(imagePath)
            # set to color and wait
            # (use non-persistent mode to help preserve flash)
            bulb.setRgb(averageColour[0],averageColour[1],averageColour[2])
            time.sleep(color_time)


    else:
        print("Can't find bulb")


if __name__ == "__main__":
    main()
