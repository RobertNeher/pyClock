import argparse
import math
import sys

import flet as ft
import flet.canvas as cv

from digit_circle import digitCircle
from tick_circle import tickCircle
from watch_face import watch_face

def main(page: ft.Page) -> None:
    parser = argparse.ArgumentParser(description='Modify data in repository',
                                    usage=f"{sys.argv[0]} [options]", allow_abbrev=False)
    parser.add_argument('-p', '--updatePeriod', nargs='?', help='update periosd in seconds (default = 1 sec.)',default="1")
    parser.add_argument('-m', '--mode', nargs='?', help='f: show watch face, s: show seconds hand, d: show date field', default='fsd')

    args = parser.parse_args()

    watchFace = False
    secondsHand = False
    dateField = False
    modes = set('fsd')

    if args.updatePeriod:
        period = int(args.updatePeriod.strip())

    if args.mode is None or any((c in modes) for c in args.mode.strip()):
        parser.print_usage()
    else:
        watchFace = "f" in args.mode.strip()
        secondsHand = "s" in args.mode.strip()
        dateField = "d" in args.mode.strip()

    radius = 200
    backgroundColor = ft.colors.BLUE_200
    digitSize = radius / 5.0
    digitStyle = ft.TextStyle(
        size = digitSize,
        color = ft.colors.BLACK54,
        weight=ft.FontWeight.BOLD
    )
    cp = watch_face(radius=radius)
    # cp.shapes.extend(digitCircle(radius=radius, digitStyle=digitStyle, digitSize=digitSize))
    cp.shapes.extend(tickCircle(radius=radius))
    page.window.width = 2.2 * radius
    page.window.height = 2.3 * radius
    page.add(ft.Container(
        height = radius * 2.0,
        width = radius * 2.0,
        bgcolor=backgroundColor,
        padding=0,
        content=cp
    ))

ft.app(main)
