import flet as ft
import flet.canvas as cv

from random_color import random_Color

def clockFace(radius: float, colors: dict, clockFace: bool, randomColor: bool):
    strokePaint = ft.Paint(
        color=ft.Colors.TRANSPARENT if not clockFace else colors["clockBoundary"],
        stroke_width=5,
        style=ft.PaintingStyle.STROKE)

    if randomColor:
        strokePaint.color = random_Color()

    canvasContent = []

    if clockFace:
        fillPaint = ft.Paint(color=colors["clockFace"], style=ft.PaintingStyle.FILL)

        canvasContent = [
            cv.Circle(radius, radius, radius * 1.03, fillPaint),
            cv.Circle(radius, radius, radius, strokePaint),
            cv.Circle(radius, radius, radius * 0.05, fillPaint)
        ]
    else:
        fillPaint = ft.Paint(color=ft.Colors.TRANSPARENT, style=ft.PaintingStyle.FILL)

        canvasContent = [
            cv.Circle(radius, radius, radius * 1.03, fillPaint),
        ]

    return cv.Canvas(
        canvasContent,
        width=float("inf"),
        expand=True,
    )
