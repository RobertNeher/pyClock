from datetime import datetime
import flet as ft
import flet.canvas as cv

from random_color import random_Color

def arrowHand(radius: float, translateX: float, translateY: float, settings: dict, randomColor: bool) -> list:
    colors = settings["colors"]
    handSettings = settings["hands"]

    secondHandPaintStroke = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=2,
        color=random_Color() if randomColor else colors["secondHand"]
    )
    secondHandPaintFill = ft.Paint(
        style=ft.PaintingStyle.FILL,
        stroke_width=2,
        color= random_Color() if randomColor else colors["secondHand"]
    )

    return  [
            #  -->cv.Circle(translateX, translateY, radius * 0.05, paint=centerDotPaint),
            cv.Path([
                cv.Path.MoveTo(
                        translateX,
                        translateY
                ),
                cv.Path.LineTo(
                    translateX + 0,
                    translateY + handSettings["secondHandWidth"] / 2.0
                ),
                cv.Path.LineTo(
                    translateX + radius * handSettings["secondHandFactor"] * 0.9,
                    translateY + handSettings["secondHandWidth"] / 2.0
                ),
                cv.Path.LineTo(
                    translateX + radius * handSettings["secondHandFactor"],
                    translateY + 0
                )
            ],
            paint=secondHandPaintStroke
        ),
        cv.Path([
                cv.Path.MoveTo(
                        translateX,
                        translateY
                ),
                cv.Path.LineTo(
                    translateX + 0,
                    translateY - handSettings["secondHandWidth"] / 2.0
                ),
                cv.Path.LineTo(
                    translateX + radius * handSettings["secondHandFactor"] * 0.9,
                    translateY - handSettings["secondHandWidth"] / 2.0
                ),
                cv.Path.LineTo(
                    translateX + radius * handSettings["secondHandFactor"],
                    translateY + 0
                )
            ],
            paint=secondHandPaintFill
        ),
        #  -->cv.Circle(translateX, translateY, radius * 0.04, paint=centerCirclePaint),
    ]


def clockHands(handType: str, radius:float, settings:dict, randomColor:bool):
    if handType == "arrow":
        return arrowHand(
            radius=radius,
            translateX=radius,
            translateY=radius,
            settings=settings,
            randomColor=randomColor
        )
    # elif handType == "rounded":
    #     return roundedHand(
    #         radius=radius,
    #         translateX=radius,
    #         translateY=radius,
    #         settings=settings,
    #         randomColor=randomColor
    #     )