import flet as ft
import flet.canvas as cv
from random_color import random_Color

def watch_face(radius: float, randomColor: bool = False):
    color = random_Color() if randomColor else ft.colors.BLACK26
    stroke_paint = ft.Paint(color=color, stroke_width=5, style=ft.PaintingStyle.STROKE)
    color = random_Color() if randomColor else ft.colors.BLACK12
    fill_paint = ft.Paint(color=color, style=ft.PaintingStyle.FILL)

    canvas = cv.Canvas(
        [
            cv.Circle(radius, radius, radius * 1.03, fill_paint),
            cv.Circle(radius, radius, radius, stroke_paint),
        ],
        width=float("inf"),
        expand=True,
    )
    color = random_Color() if randomColor else ft.colors.BLACK12
    fill_paint = ft.Paint(color=color, style=ft.PaintingStyle.FILL)

    canvas.shapes.append(
        cv.Circle(radius, radius, radius * 0.05, fill_paint),
    )

    return canvas
