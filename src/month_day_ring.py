import flet as ft
import flet.canvas as cv
import math
import calendar

from datetime import datetime

from random_color import random_Color

def monthDayRing(radius: float, settings: dict, randomColor: bool):
    colors = settings["colors"]
    today = datetime.now()
    startAngle = math.pi
    digitAngle = 0
    monthRange = calendar.monthrange(today.year, today.month)
    delta = (2.0 * math.pi)/monthRange[1]
    digit = monthRange[1]
    digitShapes = []
    digitSize = radius / 10

    radius *= 1.1

    while digitAngle <= startAngle + (2.0 * math.pi):
        x = radius * (1 + math.sin(startAngle + digitAngle))
        y = radius * (1 + math.cos(startAngle + digitAngle))

        digitStyle = ft.TextStyle(
            size = digitSize,
            color = random_Color() if randomColor else colors["monthDays"],
            weight=ft.FontWeight.NORMAL
        )

        digitShapes.append(cv.Text(
            x=(x - digitSize * math.sin(startAngle + digitAngle)),
            y=(y - digitSize * math.cos(startAngle + digitAngle)),
            text=str(digit),
            style=digitStyle,
            alignment=ft.alignment.center,
            rotate=(2.0 * math.pi) - digitAngle
        ))
        digit -= 1
        if digit <= 0:
            digit = monthRange[1]
        digitAngle += delta

    return digitShapes
