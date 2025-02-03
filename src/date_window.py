import flet as ft
import flet.canvas as cv

from datetime import datetime

from random_color import random_Color

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
        stroke_width=2,
        style=ft.PaintingStyle.STROKE
    )

    shapes = [
        cv.Rect(
            x=radius * 1.43,
            y=radius * 0.95,
            border_radius=2,
            paint=dateFramePaint,
            width=radius * 0.35,
            height=radius * 0.15,
        ),
        cv.Text(
            alignment = ft.alignment.center,
            x = radius * 1.6,
            y = radius,
            style = dateTextStyle,
            text = datetime.now().strftime(settings["dateFormat"])
        )
    ]

    return shapes