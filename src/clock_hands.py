from datetime import datetime
import flet as ft
import flet.canvas as cv

from random_color import random_Color

def clockHands(radius:float, settings:dict, randomColor:bool):
    hands = []
    minuteHandColor = random_Color() if randomColor else colors["minuteHand"]
    hourHandColor = random_Color() if randomColor else colors["hourHand"]
    secondHandColor = random_Color() if randomColor else colors["secondHand"]
    handsGeometry = settings["hands"]
    colors = settings["colors"]

    # timeSecond = datetime.now().second
    # timeMinute = datetime.now().minute
    # timeHour = datetime.now().hour
    hands.append(
        cv.Path(elements=[
                cv.Path.LineTo(
                    0,
                    hands["secondHandWidth"] / 2.0
                ),
                cv.Path.LineTo(
                    radius * settings["secondHandFactor"] * 0.8,
                    hands["secondHandWidth"] / 2.0
                ),
                cv.Path.LineTo(
                    radius * settings["secondHandFactor"],
                    0
                ),
                cv.Path.LineTo(
                    radius * settings["secondHandFactor"] * 0.8,
                    -hands["secondHandWidth"] / 2.0
                ),
                cv.Path.LineTo(
                    0,
                    -hands["secondHandWidth"] / 2.0
                ),
            ],
            paint=ft.Paint(
                style=ft.PaintingStyle.FILL,
                color=secondHandColor
            ),    
        ),
    )

    return hands