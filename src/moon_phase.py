import flet as ft
import flet.canvas as cv
from ephem import Date, Moon, next_new_moon, previous_new_moon

from random_color import random_Color
from datetime import datetime
from night_sky import nightSky


def moonPhaseOnDay() -> float:
    """Returns a floating-point number from 0-1. where 0=new, 0.5=full, 1=new"""
    date = Date(datetime.now())

    nnm = next_new_moon(date)
    pnm = previous_new_moon(date)

    lunation = (date-pnm)/(nnm-pnm)
    coverage = Moon(date).phase
    #Note that there is a ephem.Moon().phase() command, but this returns the
    #percentage of the moon which is illuminated. This is not really what we want.

    return lunation, coverage

def moonPhase(offset: ft.Offset, radius: float, settings: dict, randomColor: bool) -> ft.Control:
    colors = settings["colors"]
    coverage = 0.75 #moonPhaseOnDay()[1]

    # deltaX = 2 * radius * coverage / 100
    # deltaY = radius * coverage / 100

    # coverBorderPaint = ft.Paint(
    #     color=random_Color(tuple=False) if randomColor else colors["moonPhaseCoverBorder"],
    #     style=ft.PaintingStyle.STROKE,
    #     stroke_width = 3,
    # )
    # coverPaint = ft.Paint(
    #     color=random_Color(tuple=False) if randomColor else colors["moonPhaseCover"],
    #     style=ft.PaintingStyle.FILL,
    #     stroke_width = 3,
    # )

    return ft.Container(
        content=ft.Stack(
            [
                ft.Container(
                    content=cv.Canvas(
                        shapes=nightSky(
                            x=0,
                            y=0,
                            radius=radius*0.6,
                            settings=settings,
                            randomColor=randomColor
                        ),
                    ),
                    alignment=ft.alignment.center,
                ),
                ft.Image(
                    src="./assets/FullMoon.png",
                    color=random_Color(tuple=False) if randomColor else None,
                    color_blend_mode=ft.BlendMode.COLOR,
                    height=radius/2,
                    width=radius/2,
                    border_radius=radius/2,
                    rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
                    bottom=offset.y,
                    left=offset.x
                ),
            ],
        ),
        border_radius=5,
        width=radius * 1.25,
        height=radius * 1.25,
    )
