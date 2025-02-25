import flet as ft
import flet.canvas as cv

from datetime import datetime
from math import pi, sin, cos
from random_color import random_Color

def weekDay(radius: float, settings: dict, randomColor: bool = False) -> list:
    colors = settings["colors"]
    positionX = radius * 0.4
    positionY = radius * 0.5
    startingDay = 1 # 0 = Sunday
    digitSize = radius * 0.05
    weekDays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    radians = 0
    startAngle = 0
    dayAngle = len(weekDays) / (2*pi)
    complicationRadius=0.2 * radius
    complicationPaint = ft.Paint(
        color = random_Color if randomColor else colors["clockFace"],
        style=ft.PaintingStyle.FILL
    )

    complicationShapes = [
        cv.Circle(
            x=0, #radius, #positionX,
            y=0, #radius, #positionY,
            radius=complicationRadius,
            paint=complicationPaint,
        )
    ]

    # for i in range(0, len(weekDays) - 1):
    #     x = radius * (1.0 + sin(startAngle + dayAngle))
    #     y = radius * (1.0 + cos(startAngle + dayAngle))

    #     dayStyle = ft.TextStyle(
    #         size = digitSize,
    #         color = random_Color() if randomColor else colors["digits"],
    #         weight=ft.FontWeight.BOLD
    #     )

    #     complicationShapes.append(cv.Text(
    #         x=x - digitSize * sin(startAngle + dayAngle),
    #         y=y - digitSize * cos(startAngle + dayAngle),
    #         text=str(),
    #         style=dayStyle,
    #         alignment=ft.alignment.center,
    #         rotate=(2.0 * pi) - dayAngle
    #     ))

    return complicationShapes

def dateWindow(radius: float, settings: dict, randomColor: bool = False) -> list:
    colors = settings["colors"]

    dateTextStyle = ft.TextStyle(
        weight=ft.FontWeight.BOLD,
        color=random_Color() if randomColor else colors["dateField"],
        size = radius * 0.1,
        shadow=ft.BoxShadow(
            offset=ft.Offset(2, 2),
            color = ft.Colors.WHITE60,
            blur_style=ft.ShadowBlurStyle.INNER,
            spread_radius=3
        )
    )
    dateFramePaint = ft.Paint(
        color=random_Color() if randomColor else colors["dateFieldFrame"],
        stroke_width=3,
        style=ft.PaintingStyle.STROKE
    )
    complicationShapes = [
        cv.Rect(
            x=radius * 0.3,
            y=-radius * 0.07,
            border_radius=2,
            paint=dateFramePaint,
            width=radius * 0.35,
            height=radius * 0.14,
        ),
        cv.Text(
            alignment = ft.alignment.center,
            x = radius * 0.47,
            y = -radius * 0.01,
            style = dateTextStyle,
            text = datetime.now().strftime(settings["dateFormat"])
        )
    ]

    return complicationShapes
