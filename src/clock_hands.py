from enum import Enum, auto
import flet as ft
import flet.canvas as cv

from random_color import random_Color

class HandType(Enum):
    SECOND = auto()
    MINUTE = auto()
    HOUR = auto()

def spindle(radius: float, settings: dict, randomColor: bool):
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
        cv.Circle(0, 0, radius * 0.05, paint=centerDotPaint),
        cv.Circle(0, 0, radius * 0.04, paint=centerCirclePaint),
    ]

def arrowHand(handType: HandType, radius: float, settings: dict, randomColor: bool) -> list:
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
                        0,
                        0
                    ),
                    cv.Path.LineTo(
                        0,
                        handSettings["secondHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        radius * handSettings["secondHandFactor"] * 0.9,
                        handSettings["secondHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        radius * handSettings["secondHandFactor"],
                        0
                    ),
                    cv.Path.Close(),
                ],
                paint=secondHandPaintStroke
            ),
            cv.Path([
                    cv.Path.MoveTo(
                        0,
                        0
                    ),
                    cv.Path.LineTo(
                        0,
                        -handSettings["secondHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        radius * handSettings["secondHandFactor"] * 0.9,
                        -handSettings["secondHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        radius * handSettings["secondHandFactor"],
                        0
                    ),
                    cv.Path.Close(),
                ],
                paint=secondHandPaintFill
            )
        ]    

    if handType == HandType.MINUTE:
        return [
                cv.Path([
                    cv.Path.MoveTo(
                        0,
                        0
                    ),
                    cv.Path.LineTo(
                        0,
                        handSettings["minuteHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        radius * handSettings["minuteHandFactor"] * 0.9,
                        handSettings["minuteHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        radius * handSettings["minuteHandFactor"],
                        0
                    ),
                    cv.Path.Close(),
                ],
                paint=minuteHandPaintStroke
            ),
            cv.Path([
                    cv.Path.MoveTo(
                        0,
                        0
                    ),
                    cv.Path.LineTo(
                        0,
                        -handSettings["minuteHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        radius * handSettings["minuteHandFactor"] * 0.9,
                        -handSettings["minuteHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        radius * handSettings["minuteHandFactor"],
                        0
                    ),
                    cv.Path.Close(),
                ],
                paint=minuteHandPaintFill
            )
        ]

    if handType == HandType.HOUR:
        return [
            cv.Path([
                    cv.Path.MoveTo(
                        0,
                        0
                    ),
                    cv.Path.LineTo(
                        0,
                        handSettings["hourHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        radius * handSettings["hourHandFactor"] * 0.9,
                        handSettings["hourHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        radius * handSettings["hourHandFactor"],
                        0
                    )
                ],
                paint=hourHandPaintStroke
            ),
            cv.Path([
                    cv.Path.MoveTo(
                        0,
                        0
                    ),
                    cv.Path.LineTo(
                        0,
                        -handSettings["hourHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        radius * handSettings["hourHandFactor"] * 0.9,
                        -handSettings["hourHandWidth"] / 2.0
                    ),
                    cv.Path.LineTo(
                        radius * handSettings["hourHandFactor"],
                        0
                    )
                ],
                paint=hourHandPaintFill
            ),
        ]
