import flet as ft
import flet.canvas as cv
from math import sin, cos, pi

from random_color import random_Color

def hourRing(x: float, y: float, radius: float, colors: dict, randomColor: bool):
    startAngle = pi
    delta = (2 * pi)/12
    charAngle = -delta
    charShapes = []
    charSize = radius / 5

    for i in range(1, 13):
    # while charAngle <= startAngle + (2 * pi):
        charStyle = ft.TextStyle(
            color = random_Color() if randomColor else colors["digits"],
            size = charSize,
            weight=ft.FontWeight.NORMAL
        )

        charShapes.append(cv.Text(
            x = x + (radius + charSize) * sin(startAngle + charAngle),
            y = y + (radius + charSize) * cos(startAngle + charAngle),
            text=str(i),
            style=charStyle,
            alignment=ft.alignment.center,
            rotate=(2 * pi) - charAngle
        ))
        charAngle -= delta

    return charShapes
