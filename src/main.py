import argparse
import math
import sys

import flet as ft
import flet.canvas as cv

from random_color import random_Color
from digit_circle import digitCircle
from tick_circle import tickCircle
from watch_face import watch_face

def main(page: ft.Page) -> None:
    parser = argparse.ArgumentParser(description='Modify data in repository',
                                    usage=f"{sys.argv[0]} [options]", allow_abbrev=False)
    parser.add_argument('-p', '--updatePeriod', nargs='?', help='update periosd in seconds (default = 1 sec.)',default="1")
    parser.add_argument('-o', '--options', nargs='?', help='c: random colors,\nd: show date field,\nf: show watch face,\ns: show seconds hand', default='cdfs')

    args = parser.parse_args()

    randomColor = False
    dateField = False
    watchFace = False
    secondsHand = False

    if args.updatePeriod:
        period = int(args.updatePeriod.strip())

    randomColor = False
    dateField = False
    watchFace = False
    secondsHand = False

    for c in args.options.lower().strip():
        if c == "c":
            randomColor = True
        elif c == "f":
            watchFace = True
        elif c == "d":
            dateField = True
        elif c == "s":
            secondsHand = True
        else:
            parser.print_help()
            sys.exit()

    radius = 200
    backgroundColor = ft.colors.BLUE_200 if not randomColor else random_Color()

    cp = watch_face(radius=radius)
    cp.shapes.extend(digitCircle(radius=radius))
    cp.shapes.extend(tickCircle(radius=radius, randomColor=randomColor))
    page.window.width = 2.2 * radius
    page.window.height = 2.3 * radius
    page.add(ft.Container(
        alignment=ft.alignment.top_center,
        # alignment=ft.alignment.center, # does not work, watch is translated in y axis by radius
        height = radius * 2,
        width = radius * 2,
        bgcolor=backgroundColor,
        padding=0,
        content=cp
    ))
    page.expand=1
    page.update()

ft.app(main)
