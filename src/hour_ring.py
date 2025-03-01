import flet as ft
import flet.canvas as cv
from math import sin, cos, pi

from random_color import random_Color

def hourRing(x: float, y: float, radius: float, digitTurn: bool, colors: dict, randomColor: bool):
    startAngle = pi
    delta = (2 * pi)/12
    digitAngle = -delta
    digitShapes = []
    digitSize = radius / 5

    for i in range(1, 13):
    # while charAngle <= startAngle + (2 * pi):
        digitStyle = ft.TextStyle(
            color = random_Color() if randomColor else colors["digits"],
            size = digitSize,
            weight=ft.FontWeight.NORMAL
        )

        digitShapes.append(cv.Text(
            x = x + (radius + digitSize) * sin(startAngle + digitAngle),
            y = y + (radius + digitSize) * cos(startAngle + digitAngle),
            text=str(i),
            style=digitStyle,
            alignment=ft.alignment.center,
            rotate=((2 * pi) - digitAngle) if digitTurn else 0
        ))
        digitAngle -= delta

    return digitShapes
