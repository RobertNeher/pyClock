import flet as ft
import math
import flet.canvas as cv

def digitCircle(radius: float, digitStyle: ft.TextStyle, digitSize: float):
    startAngle = math.pi
    digitAngle = 0
    delta = (2.0 * math.pi)/12.0
    digit = 12
    digitShapes = []

    while digitAngle <= startAngle + (2.0 * math.pi):
        x = radius * (1.0 + math.sin(startAngle + digitAngle))
        y = radius * (1.0 + math.cos(startAngle + digitAngle))

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
