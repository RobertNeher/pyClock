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
    parser.add_argument('-m', '--mode', nargs='?', help='c: random colors,\nd: show date field,\nf: show watch face,\ns: show seconds hand', default='cdfs')

    args = parser.parse_args()

    randomColor = False
    dateField = False
    watchFace = False
    secondsHand = False

    modes = set('cdfs')

    if args.updatePeriod:
        period = int(args.updatePeriod.strip())

    if args.mode is None or any((c in modes) for c in args.mode.strip()):
        parser.print_usage()
    else:
        randomColor = "c" in args.mode.strip()
        watchFace = "f" in args.mode.strip()
        dateField = "d" in args.mode.strip()
        secondsHand = "s" in args.mode.strip()

    radius = 200
    backgroundColor = ft.colors.BLUE_200 if not randomColor else random_Color()

    cp = watch_face(radius=radius)
    cp.shapes.extend(digitCircle(radius=radius))
    cp.shapes.extend(tickCircle(radius=radius))
    page.window.width = 2.2 * radius
    page.window.height = 2.3 * radius
    page.add(ft.Container(
        height = radius * 2.0,
        width = radius * 2.0,
        bgcolor=backgroundColor,
        padding=0,
        content=cp,
        expand=1
    ))
    # page.width = float("inf")
    # page.expand()

ft.app(main)
