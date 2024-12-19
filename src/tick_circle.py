import flet as ft
import flet.canvas as cv
import math

def tickCircle(radius: float): #, digitStyle: ft.TextStyle, digitSize: float):
    # startAngle = math.pi
    digitAngle = 0
    delta = (2.0 * math.pi)/12.0
    tickSize = radius * 0.1
    digitShapes = []
    stroke_paint = ft.Paint(color=ft.colors.BLACK26, stroke_width=5, style=ft.PaintingStyle.STROKE)

    while digitAngle <= (2.0 * math.pi):
        digitShapes.append(cv.Line(
            # x1 = radius,
            # y1 = tickSize,
            # x2 = radius,
            # y2 = 0,
            x1 = radius * (1.0 + math.sin(digitAngle)),
            y1 = tickSize * (1.0 + math.sin(digitAngle)),
            x2 = radius * (1.0 + math.sin(digitAngle)),
            y2 = radius * (1.0 + math.sin(digitAngle)),
            paint=stroke_paint
        ))

        digitAngle += delta

    return digitShapes
