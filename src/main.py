import io
import json
import time

import flet as ft
import flet.canvas as canvas

from clock_hands import HandType, Hands, HandShape
from lunette import Lunette
from random_color import random_Color
from digit_circle import DigitCircle
from tick_circle import TickCircle, TickType

def main(page: ft.Page) -> None:
    settings = json.load(io.open("assets/settings.json", "r", encoding="UTF-8"))["settings"]

    randomColor = settings["randomColor"]
    dateField = settings["dateField"]
    face = settings["clockFace"]
    period = settings["updatePeriod"]
    radius = settings["radius"]
    colors = settings["colors"]

    def adaptRadius(e: ft.WindowEvent) -> None:
        radius = 0

        if e.control.height > (2 * radius) or e.control.width > (2 * radius):
            if e.control.height > e.control.width:
                radius = e.control.height / 2
                page.window.width = e.control.height
            else:
                radius = e.control.width / 2
                page.window.height = e.control.width

        page.expand = 1
        page.update()

    if face:
        backgroundColor = colors["clockFace"]
    else:
        backgroundColor = ft.Colors.TRANSPARENT
        page.window.bgcolor=ft.Colors.TRANSPARENT
        page.bgcolor = ft.Colors.TRANSPARENT

    page.window.width = 2.3 * radius
    page.window.height = 2.3 * radius
    page.window.resizable = True
    # page.on_resized=adaptRadius
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.expand=1

    clock = ft.Stack(
        [
            Lunette(radius=radius, colors=colors, clockFace=face, randomColor=randomColor),
            TickCircle(radius=radius, colors=colors, randomColor=randomColor, tickType=TickType.ALL),
            DigitCircle(radius=radius, colors=colors, randomColor=randomColor),
            # date field
            # moon phase
        ],
        alignment=ft.alignment.center,
    )
    page.add(clock)
    page.update()

    while True:
        clock.controls.extend([
            Hands(handType=HandType.SECOND, shape=HandShape.ARROW, settings=settings, radius=radius, randomColor=randomColor) if settings["secondHand"] else None,
            # Hands(handType=HandType.MINUTE, shape=HandShape.ARROW, settings=settings, radius=radius, randomColor=randomColor),
            # Hands(handType=HandType.HOUR, shape=HandShape.ARROW, settings=settings, radius=radius, randomColor=randomColor)
        ])
        page.update()
        del clock.controls[-1:]
        time.sleep(period)

ft.app(main)
