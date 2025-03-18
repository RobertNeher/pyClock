import flet as ft
import flet.canvas as cv

import io
import json
import sys
import time

from math import sin, cos, pi
from moon_phase import moonPhase, moonPhaseOnDay
from datetime import datetime
from random_color import random_Color


def days_in_month(date):
    next_month = datetime(int(date.year + date.month / 12), date.month % 12 + 1, 1)
    start_month = datetime(date.year, date.month, 1)
    td = next_month - start_month

    return td.days

def main(page: ft.Page):
    settings = json.load(io.open("assets/settings.json", "r", encoding="UTF-8"))["settings"]
    colors = settings["colors"]
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.WHITE
    page.window.bgcolor = ft.Colors.WHITE60
    radius = settings["radius"]
    randomColor = settings["randomColor"]
    page.window.height = radius * 2.5
    page.window.width = radius * 2.5
    # coverage = moonPhaseOnDay()[1]
    today = datetime.now()
    daysPerMonth = days_in_month(today)

    page.expand = True
    moon_Phase = moonPhase(offset=ft.Offset(radius*0.15, radius*0.15), radius=radius, settings=settings, randomColor=randomColor)

    coverPaint = ft.Paint(
        # blend_mode=ft.BlendMode.HARD_LIGHT,
        style=ft.PaintingStyle.FILL,
        # color=ft.Colors.BLACK,
        color=random_Color(tuple=False) if randomColor else colors["moonPhaseCover"],
    )
    coverBorderPaint = ft.Paint(
        stroke_cap=ft.StrokeCap.ROUND,
        stroke_width=5,
        style=ft.PaintingStyle.STROKE,
        color=random_Color(tuple=False) if randomColor else colors["moonPhaseCoverBorder"],
    )

    arc = 0

    while True: #arc < pi:
        moon_Phase.rotate = ft.transform.Rotate(arc)

        page.add(
            ft.Stack(
                controls=[
                    moon_Phase,
                    cv.Canvas(
                        shapes=[
                        ]
                    ),
                    cv.Canvas(
                        shapes=[
                            cv.Circle(
                                x=radius*0.95,
                                y=radius*0.5,
                                radius=radius*0.26,
                                paint=coverBorderPaint
                            ),
                            cv.Circle(
                                x=radius*0.3,
                                y=radius*0.5,
                                radius=radius*0.26,
                                paint=coverBorderPaint
                            ),
                            cv.Rect(
                                x=radius*0.035,
                                y=radius*0.5,
                                width=radius*1.18,
                                height=radius*0.75,
                                paint=coverPaint
                            ),
                            cv.Rect(
                                x=radius*0.035,
                                y=radius*0.5,
                                width=radius*1.18,
                                height=radius*0.75,
                                paint=coverBorderPaint
                            ),
                            cv.Circle(
                                x=radius*0.95,
                                y=radius*0.5,
                                radius=radius*0.26,
                                paint=coverPaint
                            ),
                            cv.Circle(
                                x=radius*0.3,
                                y=radius*0.5,
                                radius=radius*0.26,
                                paint=coverPaint
                            ),
                            # cv.Arc(
                            #     x=0,#radius*0.95,
                            #     y=0,#radius*0.5,
                            #     width=radius*0.26,
                            #     height=radius*0.26,
                            #     paint=coverBorderPaint,

                            # ),
                        ]
                    ),
            ])

        )
        page.update()


        time.sleep(0.1)
        page.controls.clear()

        arc += pi/daysPerMonth


# if __name__ == "__main__":

ft.app(main)
