import flet as ft
import flet.canvas as cv

from random_color import random_Color

def Lunette(radius: float, colors: dict, clockFace: bool = True, randomColor: bool = False) -> cv.Canvas:
    strokePaint = ft.Paint(
        color=ft.Colors.TRANSPARENT if not clockFace else random_Color() if randomColor else colors["clockFace"],
        stroke_width=5,
        style=ft.PaintingStyle.STROKE)

    lunetteContent = []

    if clockFace:
        fillPaint = ft.Paint(color=colors["clockFace"], style=ft.PaintingStyle.FILL)

        lunetteContent = [
            cv.Circle(radius, 0, radius * 1.03, fillPaint),
            cv.Circle(radius, 0, radius * 1.03, strokePaint),
        ]
    else:
        fillPaint = ft.Paint(color=ft.Colors.TRANSPARENT, style=ft.PaintingStyle.FILL)

        lunetteContent = [
            cv.Circle(radius, 0, radius * 1.03, fillPaint),
        ]

    return cv.Canvas(
        lunetteContent,
        width=float("inf"),
        expand=True,
    )
