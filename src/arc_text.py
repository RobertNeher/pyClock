import flet as ft
import flet.canvas as cv
from math import pi, sin, cos

from random_color import random_Color

def arcText(x: float, y: float, text: str, radius: float, colors: dict, randomColor: bool) -> list:
    startAngle = pi
    charAngle = 0
    delta = (2 * pi)/float(len(text))
    chars = len(text)
    charShapes = []
    charSize = radius / 10.0

    for i in range(0, len(text)):
    # while charAngle <= startAngle + (2 * pi):
        charStyle = ft.TextStyle(
            color = random_Color() if randomColor else colors["digits"],
            size = charSize,
            weight=ft.FontWeight.NORMAL
        )

        # x = radius * (1.0 + sin(startAngle + charAngle)) - radius
        # y = radius * (1.0 + cos(startAngle + charAngle)) - radius
        x = radius * sin(startAngle + charAngle)
        y = radius * cos(startAngle + charAngle)

        charShapes.append(cv.Text(
            x = x + charSize * sin(startAngle + charAngle),
            y = y + charSize * cos(startAngle + charAngle),
            text=text[i],
            style=charStyle,
            alignment=ft.alignment.center,
            rotate=(2 * pi) - charAngle
        ))
        charAngle -= delta

    return charShapes
