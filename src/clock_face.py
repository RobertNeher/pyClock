import flet as ft

from digit_circle import DigitCircle
from tick_types import TickType
from lunette import Lunette
from tick_circle import TickCircle

def clockFace(radius: float, colors: dict, clock_face: bool, randomColor: bool) -> ft.Control:
    face = ft.Container(
        height= 2 * radius,
        width = 2 * radius,
        bgcolor=colors["clockFace"] if clock_face else ft.Colors.TRANSPARENT
    )

    if clock_face:
        face.content = ft.Stack(
            alignment=ft.alignment.center,
            controls=[
                Lunette(radius=radius, colors=colors, clockFace=clockFace, randomColor=randomColor),
                TickCircle(radius=radius, colors=colors, randomColor=randomColor, tickType=TickType.ALL),
                DigitCircle(radius=radius, colors=colors, randomColor=randomColor)
            ]
        )
