# import argparse
import io
import math
import sys
import json

import flet as ft
import flet.canvas as cv

from random_color import random_Color
from digit_circle import digitCircle
from tick_circle import tickCircle
from clock_face import clockFace

def main(page: ft.Page) -> None:
    settings = json.load(io.open("assets/settings.json", "r", encoding="UTF-8"))["settings"]

    randomColor = settings["randomColor"]
    dateField = settings["dateField"]
    face = settings["clockFace"]
    secondsHand = settings["secondHand"]
    period = settings["updatePeriod"]
    radius = settings["radius"]
    colors = settings["colors"]

    if face:
        backgroundColor = colors["clockFace"] if not randomColor else random_Color()
    else:
        backgroundColor = ft.Colors.TRANSPARENT

    cp = clockFace(radius=radius, colors=colors, clockFace=face, randomColor=randomColor)

    if face:
        cp.shapes.extend(tickCircle(radius=radius, colors=colors, randomColor=randomColor))
        cp.shapes.extend(digitCircle(radius=radius, colors=colors, randomColor=randomColor))

    page.window.width = 2.2 * radius
    page.window.height = 2.3 * radius
    page.add(ft.Container(
        alignment=ft.alignment.top_center,
        height = radius * 2,
        width = radius * 2,
        bgcolor=backgroundColor,
        padding=0,
        content=cp
    ))
    page.expand=1
    page.update()

ft.app(main)
