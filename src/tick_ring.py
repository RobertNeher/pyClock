import flet as ft
import flet.canvas as cv
from math import cos, sin, pi

from random_color import random_Color

def tickRing(radius: float, colors: dict, randomColor: bool = False): #, digitStyle: ft.TextStyle, digitSize: float):
    tickSizeHour = radius * 0.1
    tickSizeMinute = radius * 0.05
    digitShapes = []
    strokePaint = ft.Paint(color=colors["hourTick"], stroke_width=5, style=ft.PaintingStyle.STROKE)

    for i in range(1, 60):
        radiant = float(i) * (2 * pi / 60.0)

        x1 = radius * sin(radiant)
        y1 = radius * cos(radiant)

        if i % 5 == 0: # hour tick
            x2 = x1 - tickSizeHour * sin(radiant)
            y2 = y1 - tickSizeHour * cos(radiant)
            strokePaint = ft.Paint(
                color=random_Color() if randomColor else colors["hourTick"],
                stroke_width=8,
                style=ft.PaintingStyle.STROKE
            )
        else: # minute tick
            x2 = x1 - tickSizeMinute * sin(radiant)
            y2 = y1 - tickSizeMinute * cos(radiant)

            strokePaint = ft.Paint(
                color=random_Color() if randomColor else colors["minuteTick"],
                stroke_width=5,
                style=ft.PaintingStyle.STROKE
            )

        digitShapes.append(
            cv.Line(
                x1 = radius + x1,
                y1 = radius + y1,
                x2 = radius + x2,
                y2 = radius + y2,
                paint=strokePaint
            )
        )

    return digitShapes
