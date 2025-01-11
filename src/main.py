import io
import json
import keyboard
import math
from datetime import datetime

import flet as ft

from clock_hands import clockHands
from lunette import Lunette
from random_color import random_Color
from digit_circle import digitCircle
from tick_circle import tickCircle
from clock_face import clockFace

def main(page: ft.Page) -> None:
    time = datetime.now()
    settings = json.load(io.open("assets/settings.json", "r", encoding="UTF-8"))["settings"]

    randomColor = settings["randomColor"]
    dateField = settings["dateField"]
    face = settings["clockFace"]
    secondsHand = settings["secondHand"]
    # period = settings["updatePeriod"]
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
        backgroundColor = random_Color() if not randomColor else colors["clockFace"]
        clockFaceCanvas = clockFace(radius=radius, colors=colors, clockFace=face, randomColor=randomColor)
        clockFaceCanvas.shapes.extend(tickCircle(radius=radius, colors=colors, randomColor=randomColor))
        clockFaceCanvas.shapes.extend(digitCircle(radius=radius, colors=colors, randomColor=randomColor))
        # date field
        # moon phase
    else:
        backgroundColor = ft.Colors.TRANSPARENT
        page.window.bgcolor=ft.Colors.TRANSPARENT
        page.bgcolor = ft.Colors.TRANSPARENT




    page.window.width = 2.2 * radius
    page.window.height = 2.3 * radius
    page.window.resizable = True
    page.on_resized=adaptRadius
    page.add(ft.Stack(
            [
                Lunette(radius=radius, colors=colors, clockFace: face, randomColor:randomColor),
                clockFaceCanvas,
            ]
        )
    )
    page.expand=1
    page.update()
    page.add()

        clockFaceCanvas.shapes.extend(
            clockHands(
                radiant=2.0 * math.pi / 60 * time.second,
                handType="arrow",
                radius=radius,
                randomColor=randomColor,
                settings=settings
            )
        )

ft.app(main)
