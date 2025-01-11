import flet as ft
import flet.canvas as cv

from random_color import random_Color

def Lunette(radius: float, colors: dict, clockFace: bool, randomColor: bool):
    strokePaint = ft.Paint(
        color=ft.Colors.TRANSPARENT if not clockFace else random_Color() if randomColor else colors["clockFace"],
        stroke_width=5,
        style=ft.PaintingStyle.STROKE)

    lunetteContent = []

    if clockFace:
        fillPaint = ft.Paint(color=colors["clockFace"], style=ft.PaintingStyle.FILL)

        lunetteContent = [
            cv.Circle(radius, radius, radius * 1.07, fillPaint),
            cv.Circle(radius, radius, radius * 1.04, strokePaint),
        ]
    else:
        fillPaint = ft.Paint(color=ft.Colors.TRANSPARENT, style=ft.PaintingStyle.FILL)

        lunetteContent = [
            cv.Circle(radius, radius, radius * 1.07, fillPaint),
        ]

    return cv.Canvas(
        lunetteContent,
        width=float("inf"),
        expand=True,
    )
