"""Example to cycle a bulb between colors in a list, with a smooth fade between.
Assumes the bulb is already on.
The python file with the Flux LED wrapper classes should live in
the same folder as this script
"""
from itertools import cycle
import os
import sys
import time
from flux_led import BulbScanner, WifiLedBulb

this_folder = os.path.dirname(os.path.realpath(__file__))
sys.path.append(this_folder)

def main():

    # Find the bulb on the LAN
    scanner = BulbScanner()
    scanner.scan(timeout=4)

    # Specific ID/MAC of the bulb to set
    bulb_info = scanner.getBulbInfoByID("ACCF235FFFFF")

    if bulb_info:

        bulb = WifiLedBulb(bulb_info["ipaddr"])


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

            bulb.refreshState()


    else:
        print("Can't find bulb")


if __name__ == "__main__":
    main()
