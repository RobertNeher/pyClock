from datetime import datetime
import flet as ft
import flet.canvas as cv

from random_color import random_Color

def arrowHand(radiant: float, radius: float, translateX: float, translateY: float, settings: dict, randomColor: bool) -> list:
    colors = settings["colors"]
    handSettings = settings["hands"]

    handsCanvas = cv.Canvas
    handsCanvas.shapes = []

    centerDotPaint = ft.Paint(
        style=ft.PaintingStyle.FILL,
        color=random_Color() if randomColor else colors["centerDot"]
    )
    centerCirclePaint = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=3,
        color=random_Color() if randomColor else colors["centerTop"]
    )
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
    handsShape = [
            cv.Circle(translateX, translateY, radius * 0.05, paint=centerDotPaint),
            cv.Path([
                cv.Path.MoveTo(
                    translateX,
                    translateY
                ),
                cv.Path.LineTo(
                    translateX + 0,
                    translateY + handSettings["secondHandWidth"] / 2
                ),
                cv.Path.LineTo(
                    translateX + radius * handSettings["secondHandFactor"] * 0.95,
                    translateY + handSettings["secondHandWidth"] / 2
                ),
                cv.Path.LineTo(
                    translateX + radius * handSettings["secondHandFactor"],
                    translateY + 0
                ),
                cv.Path.Close()
            ],
            paint=secondHandPaintFill
        ),
        cv.Path([
                cv.Path.MoveTo(
                    translateX,
                    translateY
                ),
                cv.Path.LineTo(
                    translateX + 0,
                    translateY - handSettings["secondHandWidth"] / 2
                ),
                cv.Path.LineTo(
                    translateX + radius * handSettings["secondHandFactor"] * 0.95,
                    translateY - handSettings["secondHandWidth"] / 2
                ),
                cv.Path.LineTo(
                    translateX + radius * handSettings["secondHandFactor"],
                    translateY + 0
                ),
                cv.Path.Close()
            ],
            paint=secondHandPaintFill
        ),
        cv.Circle(translateX, translateY, radius * 0.04, paint=centerCirclePaint),
    ]

    return handsShape


def clockHands(radiant: float, handType: str, radius:float, settings:dict, randomColor:bool):
    if handType == "arrow":
        return arrowHand(
            radiant=radiant,
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