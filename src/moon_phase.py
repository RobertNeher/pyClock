import flet as ft
import flet.canvas as cv
import calendar
from ephem import Date, Moon, next_new_moon, previous_new_moon 

from random_color import random_Color
from datetime import datetime
from night_sky import nightSky


def moonPhaseOnDay() -> float:
  """Returns a floating-point number from 0-1. where 0=new, 0.5=full, 1=new"""
  #Ephem stores its date numbers as floating points, which the following uses
  #to conveniently extract the percent time between one new moon and the next
  #This corresponds (somewhat roughly) to the phase of the moon.

  #Use Year, Month, Day as arguments
  date = Date(datetime.now())

  nnm = next_new_moon(date)
  pnm = previous_new_moon(date)

  lunation = (date-pnm)/(nnm-pnm)
  coverage = Moon(date).phase
  #Note that there is a ephem.Moon().phase() command, but this returns the
  #percentage of the moon which is illuminated. This is not really what we want.

  return lunation, coverage

def moonPhase(radius: float, settings: dict, randomColor: bool) -> ft.Control:
	colors = settings["colors"]
	coverage = moonPhaseOnDay()[1]
  
	deltaX = 2 * radius * coverage / 100
	deltaY = radius * coverage / 100

	coverBorderPaint = ft.Paint(
		color=random_Color(tuple=False) if randomColor else colors["moonPhaseCoverBorder"],
		style=ft.PaintingStyle.STROKE,
		stroke_width = 3,
	)
	coverPaint = ft.Paint(
		color=random_Color(tuple=False) if randomColor else colors["moonPhaseCover"],
		style=ft.PaintingStyle.FILL,
		stroke_width = 3,
	)

	return ft.Container(
        content=ft.Stack(
            [
                ft.Container(
                    content=cv.Canvas(
                        shapes=nightSky(
                            x=0,
                            y=0,
                            radius=radius/2,
                            settings=settings,
                            randomColor=randomColor
                        ),
                    ),
                    alignment=ft.alignment.center,
                    bottom=radius/2,
                    left=radius/1.75
                ),
                ft.Image(
                    src="./assets/FullMoon.png",
                    color=random_Color(tuple=False) if randomColor else None,
                    color_blend_mode=ft.BlendMode.COLOR,
                    height=radius/2,
                    width=radius/2,
                    border_radius=radius/2,
                    rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
                    left=0,
                    bottom=radius * 0.15,
                ),
                ft.Container(
                    content=cv.Canvas(
                        shapes=[
                          cv.Circle(
							x=radius/4,
							y=radius/4,
							radius=radius/4,
							paint=coverPaint
                          )
                        ]
                    ),
                    alignment=ft.alignment.center_left,
                    left=0,
                    bottom=radius*0.65
                ),
                ft.Container(
                    content=cv.Canvas(
                        shapes=[
                          cv.Circle(
							x=radius/4,
							y=radius/4,
							radius=radius/4,
							paint=coverBorderPaint
                          )
                        ]
                    ),
                    alignment=ft.alignment.center_left,
                    left=0,
                    bottom=radius*0.65
                ),
                ft.Container(
                    content=cv.Canvas(
                        shapes=[
                          cv.Circle(
							x=radius/4,
							y=radius/4,
							radius=radius/4,
							paint=coverPaint
                          )
                        ]
                    ),
                    alignment=ft.alignment.center_left,
                    right=radius*0.5,
                    bottom=radius*0.65
                ),
               ft.Container(
                    content=cv.Canvas(
                        shapes=[
                          cv.Circle(
							x=radius/4,
							y=radius/4,
							radius=radius/4,
							paint=coverBorderPaint
                          )
                        ]
                    ),
                    alignment=ft.alignment.center_left,
                    right=radius*0.5,
                    bottom=radius*0.65
                ),
                ft.Container(
                    content=cv.Canvas(
                        shapes=[
                          cv.Rect(
							x=0,
							y=0,
                            width=2*radius,
                            height=radius/2,
							paint=coverPaint,
                          )
                        ]
                    ),
                    alignment=ft.alignment.center,
                    left=-radius*0.05,
                    bottom=radius*0.5
                ),
            ],
        ),
        border_radius=5,
        padding=10,
        width=radius * 1.25,
        height=radius * 1.25,
    )
