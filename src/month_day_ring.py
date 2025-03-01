import flet as ft
import flet.canvas as cv
import calendar

from datetime import datetime
from math import sin, cos, pi

from random_color import random_Color

def monthDayRing(x: float, y: float, radius: float, colors: dict, randomColor: bool):
    today = datetime.now()
    monthRange = calendar.monthrange(today.year, today.month)
    startAngle = pi
    delta = (2.0 * pi)/monthRange[1]
    digitAngle = -delta

    digitShapes = []
    digitSize = radius / 10

    radius *= 1.1

    for i in range(1, monthRange[1] + 1):
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
            rotate=(2 * pi) - digitAngle
        ))
        digitAngle -= delta

    return digitShapes
