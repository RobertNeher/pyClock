import flet as ft
import flet.canvas as cv

from datetime import datetime

from random_color import random_Color

def dateWindow(radius: float, colors: dict, randomColor: bool = False) -> list:
    dateTextStyle = ft.TextStyle(
        weight=ft.FontWeight.NORMAL,
        color=random_Color() if randomColor else colors["dateField"],
        size=radius * 0.3
    )

    dateFramePaint = ft.Paint(
        color=colors["dateFieldFrame"],
        stroke_width=2,
        style=ft.PaintingStyle.STROKE
    )

    shapes = [
        cv.Rect(
            x=radius * 0.85,
            y=-radius * 0.5,
            border_radius=2,
            paint=dateFramePaint,
            width=radius * 0.4,
            height=radius * 0.5,
        ),
        # cv.Text(
        #     alignment=ft.alignment.center,
        #     x=
        # )
    ]

    return shapes