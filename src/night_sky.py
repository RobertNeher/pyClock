import flet as ft
import flet.canvas as cv
import random
from random_color import random_Color
from math import sqrt

def nightSky(x: float, y: float, radius: float, settings: dict, randomColor: bool) -> list:
    colors = settings["colors"]
    nighthSkyShapes = []

    skyPaint = ft.Paint(
        color=random_Color(tuple=False) if randomColor else colors["nightSky"],
        style=ft.PaintingStyle.FILL,
        # blend_mode=ft.BlendMode.COLOR,
    )
    # Dark Sky
    nighthSkyShapes = [
       cv.Circle(
          x=x,
          y=y,
          radius=radius,
          paint=skyPaint,
        ),
    ]
    # Stars
    i = 0
    limit = random.randint(1, settings["maxStars"])
    while i <= limit:
        _x = x+random.uniform(-radius, radius)
        _y = y+random.uniform(-radius, radius)
        _h = sqrt(_x**2 + _y**2)
        
        if _h > float(radius):
            limit += 1
        else:
            starPaint = ft.Paint(
                color=random_Color(tuple=False) if randomColor else colors["stars"],
                style = ft.PaintingStyle.FILL,
                blend_mode=ft.BlendMode.LIGHTEN,
            )

            nighthSkyShapes.append(
                cv.Circle(
                    x=_x,
                    y=_y,
                    paint=starPaint,
                    radius=2,
                )
            )

        i += 1

    return nighthSkyShapes
