import flet as ft
import flet.canvas as cv
import calendar

from datetime import datetime
from math import sin, cos, pi

from random_color import random_Color

def weekDayRing(x: float, y: float, radius: float, textTurn: bool, colors: dict, randomColor: bool):
    weekDays = ["Mon", "Die", "Mit", "Don", "Fri", "Sam", "Son"]
    today = datetime.now()
    monthRange = calendar.monthrange(today.year, today.month)
    startAngle = pi
    delta = (2.0 * pi)/len(weekDays)
    digitAngle = -delta

    digitShapes = []
    digitSize = radius / 3

    for i in range(1, len(weekDays) + 1):
        digitStyle = ft.TextStyle(
            color = random_Color() if randomColor else colors["digits"],
            size = digitSize,
            weight=ft.FontWeight.NORMAL
        )

        digitShapes.append(cv.Text(
            x = x + (radius + digitSize) * sin(startAngle + digitAngle),
            y = y + (radius + digitSize) * cos(startAngle + digitAngle),
            text=weekDays[i-1],
            style=digitStyle,
            alignment=ft.alignment.center,
            rotate=((2 * pi) - digitAngle) if textTurn else 0
        ))
        digitAngle -= delta

    return digitShapes
