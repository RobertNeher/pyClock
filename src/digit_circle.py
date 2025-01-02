import flet as ft
import flet.canvas as cv
import math

from random_color import random_Color

def digitCircle(radius: float, colors: dict, randomColor: bool):
    startAngle = math.pi
    digitAngle = 0
    delta = (2.0 * math.pi)/12.0
    digit = 12
    digitShapes = []
    digitSize = radius / 5.0

        while digitAngle <= startAngle + (2.0 * math.pi):
            digitStyle = ft.TextStyle(
                color = random_Color() if randomColor else colors["digits"],
                size = digitSize,
                weight=ft.FontWeight.BOLD
            )

        x = radius * (1.0 + math.sin(startAngle + digitAngle))
        y = radius * (1.0 + math.cos(startAngle + digitAngle))

        digitStyle = ft.TextStyle(
            size = digitSize,
            color = random_Color() if randomColor else ft.colors.BLACK54,
            weight=ft.FontWeight.BOLD
        )

        digitShapes.append(cv.Text(
            x=x - digitSize * math.sin(startAngle + digitAngle),
            y=y - digitSize * math.cos(startAngle + digitAngle),
            text=str(digit),
            style=digitStyle,
            alignment=ft.alignment.center,
            rotate=(2.0 * math.pi) - digitAngle
        ))
        digit -= 1
        if digit <= 0:
            digit = 12
        digitAngle += delta

    return digitShapes
