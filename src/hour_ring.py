import flet as ft
import flet.canvas as cv
from math import sin, cos, pi

from random_color import random_Color

def hourRing(radius: float, digitTurn: bool, colors: dict, randomColor: bool):
    digitShapes = []
    digitSize = radius / 7


    for i in range(12, 0, -1):
        radiant = float(i) * (2 * pi / 12.0) - pi/2
        x = (radius - digitSize - 10) * cos(radiant)
        y = (radius - digitSize - 10) * sin(radiant)

        digitStyle = ft.TextStyle(
            color = random_Color() if randomColor else colors["digits"],
            size = digitSize,
            weight=ft.FontWeight.NORMAL
        )

        digitShapes.append(cv.Text(
            x=radius + x,
            y=radius + y,
            text=str(i),
            style=digitStyle,
            alignment=ft.alignment.center,
            rotate=radiant + pi/2 if digitTurn else 0
        ))

    return digitShapes
