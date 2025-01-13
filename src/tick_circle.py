import flet as ft
import flet.canvas as cv
import math

from enum import Flag, auto

from random_color import random_Color
class TickType(Flag):
    HOURS_ONLY = auto()
    MINUTES_ONLY = auto()
    ALL = HOURS_ONLY | MINUTES_ONLY


def TickCircle(radius: float, colors: dict, randomColor: bool = False, tickType: TickType = TickType.ALL) -> cv.Canvas: #, digitStyle: ft.TextStyle, digitSize: float):
    tickSizeHour = radius * 0.1
    tickSizeMinute = radius * 0.05
    ticksShapes = []
    strokePaint = ft.Paint(
        color=colors["hourTick"],
        stroke_width=5,
        style=ft.PaintingStyle.STROKE
    )

    hourTickWidth = 8
    minuteTickWidth = 5

    for i in range(0, 59):
        radiant = float(i) * (2 * math.pi / 60.0)

        x1 = radius * math.sin(radiant)
        y1 = radius * math.cos(radiant)

        if (i % 5 == 0) and tickType in [TickType.HOURS_ONLY, TickType.ALL]: # hour tick
            x2 = x1 - tickSizeHour * math.sin(radiant)
            y2 = y1 - tickSizeHour * math.cos(radiant)

            strokePaint = ft.Paint(
                color=random_Color() if randomColor else colors["hourTick"],
                stroke_width=hourTickWidth,
                style=ft.PaintingStyle.STROKE
            )

            ticksShapes.append(
                cv.Line(
                    x1 = radius + x1,
                    y1 = y1,
                    x2 = radius + x2,
                    y2 = y2,
                    paint=strokePaint
                )
            )

        elif tickType in [TickType.MINUTES_ONLY, TickType.ALL]: # minute tick
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
                    y1 = y1,
                    x2 = radius + x2,
                    y2 = y2,
                    paint=strokePaint
                )
            )

    return cv.Canvas(
        shapes = ticksShapes,
        width=float("inf"),
        expand=True
    )
