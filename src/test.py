import flet as ft

import io
import json
import sys
import time

from math import sin, cos, pi
from moon_phase import moonPhase, moonPhaseOnDay
from datetime import datetime

def days_in_month(date):
    next_month = datetime(int(date.year + date.month / 12), date.month % 12 + 1, 1)
    start_month = datetime(date.year, date.month, 1)
    td = next_month - start_month

    return td.days

def main(page: ft.Page):
    settings = json.load(io.open("assets/settings.json", "r", encoding="UTF-8"))["settings"]
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.WHITE
    page.window.bgcolor = ft.Colors.WHITE60
    radius = settings["radius"]
    randomColor = settings["randomColor"]
    page.window.height = radius * 2.5
    page.window.width = radius * 2.5
    # coverage = moonPhaseOnDay()[1]
    today = datetime.now()
    daysPerMonth = days_in_month(today)

    page.expand = True
    offset = ft.Offset(-radius / 4, radius/4)

    arc = 0

    while arc < pi:
        left = -(offset.x + radius/2 * cos (arc))
        bottom = (offset.y + radius/2 * sin(arc))

        page.add(
            moonPhase(left=left, bottom=bottom, radius=radius, settings=settings, randomColor=randomColor)
        )
        page.update()

        time.sleep(0.5)
        page.controls.clear()

        arc += pi/daysPerMonth

    sys.exit()


# if __name__ == "__main__":

ft.app(main)
