from enum import Enum, auto
import flet as ft
import flet.canvas as cv

from random_color import random_Color

class HandType(Enum):
    SECOND = auto()
    MINUTE = auto()
    HOUR = auto()

def spindle(radius: float, translateX: float, translateY: float, settings: dict, randomColor: bool):
    colors = settings["colors"]

    centerDotPaint = ft.Paint(
        style=ft.PaintingStyle.FILL,
        color=random_Color() if randomColor else colors["secondHand"]
    )
    centerCirclePaint = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=1,
        color=random_Color() if randomColor else colors["secondHand"]
    )

    return [
        cv.Circle(translateX, translateY, radius * 0.05, paint=centerDotPaint),
        cv.Circle(translateX, translateY, radius * 0.04, paint=centerCirclePaint),
    ]

def arrowHand(handType: HandType, radius: float, translateX: float, translateY: float, settings: dict, randomColor: bool) -> list:
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

    minuteHandPaintStroke = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=2,
        color=random_Color() if randomColor else colors["minuteHand"]
    )
    minuteHandPaintFill = ft.Paint(
        style=ft.PaintingStyle.FILL,
        stroke_width=2,
        color= random_Color() if randomColor else colors["minuteHand"]
    )

    hourHandPaintStroke = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=2,
        color=random_Color() if randomColor else colors["hourHand"]
    )
    hourHandPaintFill = ft.Paint(
        style=ft.PaintingStyle.FILL,
        stroke_width=2,
        color= random_Color() if randomColor else colors["hourHand"]
    )

    if handType == HandType.SECOND:
        return  [
            # second hand
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
            )
        ]    

    if handType == HandType.MINUTE:
        return [
                cv.Path([
                    cv.Path.MoveTo(
                            translateX,
                            translateY
                    ),
                    cv.Path.LineTo(
                        translateX + 0,
                        translateY + handSettings["minuteHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        translateX + radius * handSettings["minuteHandFactor"] * 0.9,
                        translateY + handSettings["minuteHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        translateX + radius * handSettings["minuteHandFactor"],
                        translateY + 0
                    )
                ],
                paint=minuteHandPaintStroke
            ),
            cv.Path([
                    cv.Path.MoveTo(
                            translateX,
                            translateY
                    ),
                    cv.Path.LineTo(
                        translateX + 0,
                        translateY - handSettings["minuteHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        translateX + radius * handSettings["minuteHandFactor"] * 0.9,
                        translateY - handSettings["minuteHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        translateX + radius * handSettings["minuteHandFactor"],
                        translateY + 0
                    )
                ],
                paint=minuteHandPaintFill
            )
        ]

    if handType == HandType.HOUR:
        return [
            cv.Path([
                    cv.Path.MoveTo(
                            translateX,
                            translateY
                    ),
                    cv.Path.LineTo(
                        translateX + 0,
                        translateY + handSettings["hourHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        translateX + radius * handSettings["hourHandFactor"] * 0.9,
                        translateY + handSettings["hourHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        translateX + radius * handSettings["hourHandFactor"],
                        translateY + 0
                    )
                ],
                paint=hourHandPaintStroke
            ),
            cv.Path([
                    cv.Path.MoveTo(
                            translateX,
                            translateY
                    ),
                    cv.Path.LineTo(
                        translateX + 0,
                        translateY - handSettings["hourHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        translateX + radius * handSettings["hourHandFactor"] * 0.9,
                        translateY - handSettings["hourHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        translateX + radius * handSettings["hourHandFactor"],
                        translateY + 0
                    )
                ],
                paint=hourHandPaintFill
            ),
        ]

def handsSpindle(radius:float, settings:dict, randomColor:bool):
    return spindle(
        radius=radius,
        translateX=0,
        translateY=0,
        settings=settings,
        randomColor=randomColor
    )

def clockSecondHands(radius:float, settings:dict, randomColor:bool):
    return arrowHand(
        handType=HandType.SECOND,
        radius=radius,
        translateX=0,
        translateY=0,
        settings=settings,
        randomColor=randomColor
    )

def clockMinuteHands(radius:float, settings:dict, randomColor:bool):
    return arrowHand(
        handType=HandType.MINUTE,
        radius=radius,
        translateX=0,
        translateY=0,
        settings=settings,
        randomColor=randomColor
    )


def clockHourHands(radius:float, settings:dict, randomColor:bool):
    return arrowHand(
        handType=HandType.HOUR,
        radius=radius,
        translateX=0,
        translateY=0,
        settings=settings,
        randomColor=randomColor
    )
