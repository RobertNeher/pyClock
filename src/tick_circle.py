import flet as ft
import flet.canvas as cv
import math

from enum import Enum
from random_color import random_Color
from tick_types import TickType



def TickCircle(radius: float, colors: dict, randomColor: bool = False, tickType: TickType = TickType.ALL): #, digitStyle: ft.TextStyle, digitSize: float):
    tickSizeHour = radius * 0.1
    tickSizeMinute = radius * 0.05
    ticksShapes = []
    strokePaint = ft.Paint(color=colors["hourTick"], stroke_width=5, style=ft.PaintingStyle.STROKE)

    hourTickWidth = 8
    minuteTickWidth = 5

    for i in range(0, 59):
        radiant = float(i) * (2 * math.pi / 60.0)

        x1 = radius * math.sin(radiant)
        y1 = radius * math.cos(radiant)
        x2 = x1 - tickSizeMinute * math.sin(radiant)
        y2 = y1 - tickSizeMinute * math.cos(radiant)

        if tickType == TickType.HOURS_ONLY and i % 5 == 0: # hour tick
            x2 = x1 - tickSizeHour * math.sin(radiant)
            y2 = y1 - tickSizeHour * math.cos(radiant)

            strokePaint = ft.Paint(
                color=random_Color() if randomColor else colors["hourTick"],
                stroke_width=hourTickWidth,
                style=ft.PaintingStyle.STROKE
            )
        elif tickType == TickType.MINUTES_ONLY or tickType == TickType.ALL: # minute tick
            x2 = x1 - tickSizeMinute * math.sin(radiant)
            y2 = y1 - tickSizeMinute * math.cos(radiant)

            strokePaint = ft.Paint(
                color=random_Color() if randomColor else colors["minuteTick"],
                stroke_width=minuteTickWidth,
                style=ft.PaintingStyle.STROKE
            )

        ticksShapes.append(
            cv.Line(
                x1 = radius + x1,
                y1 = radius + y1,
                x2 = radius + x2,
                y2 = radius + y2,
                paint=strokePaint
            )
        )

    return cv.Canvas(
        shapes = ticksShapes,
        width=float("inf"),
        expand=True
    )
