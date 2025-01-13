import copy

from math import pi
from enum import Flag, auto
from datetime import datetime

import flet as ft
import flet.canvas as cv

from random_color import random_Color
class HandType(Flag):
    HOUR = auto()
    MINUTE = auto()
    SECOND = auto()
    ALL = HOUR | MINUTE | SECOND

class HandShape(Flag):
    ARROW = auto()
    ROUNDED = auto()
    ELLIPTICAL = auto()


def arrowHand(handType: HandType, radius: float, settings: dict, randomColor: bool) -> ft.Control:
    colors = settings["colors"]
    handSettings = settings["hands"]

    translateX = 0
    translateY = 0

    time = datetime.now()

    centerDotPaint = ft.Paint(
        style=ft.PaintingStyle.FILL,
        color=random_Color() if randomColor else colors["centerDot"]
    )
    centerCirclePaint = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=3,
        color=random_Color() if randomColor else colors["centerTop"]
    )

    handPaintStroke = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=2
    )

    angle = -pi/2

    if handType == HandType.SECOND:
        handWidth = handSettings["secondHandWidth"]
        handLength = radius * handSettings["secondHandFactor"]
        handPaintStroke.color = random_Color() if randomColor else colors["secondHand"]
        angle += (2 * pi) / 60 * time.second

    elif handType == HandType.MINUTE:
        handWidth = handSettings["minuteHandWidth"]
        handLength = radius * handSettings["minuteHandFactor"]
        handPaintStroke.color = random_Color() if randomColor else colors["minuteHand"]
        angle += (2 * pi) / 60 * time.minute

    elif handType == HandType.HOUR:
        handWidth = handSettings["hourHandWidth"]
        handLength = radius * handSettings["hourHandFactor"]
        handPaintStroke.color = random_Color() if randomColor else colors["hourHand"]
        angle += (2 * pi) / 12 * (time.hour % 12)

    else: # never reachable
        handWidth = radius * 0.05
        handLength = radius * 0.95
        angle += 0

    # translateX -= handWidth
    translateY -= handWidth
    handPaintFill = copy.deepcopy(handPaintStroke)
    handPaintFill.style = ft.PaintingStyle.FILL
    handPaintFill.color = random_Color() if randomColor else colors["hourHand"]
    hand = cv.Canvas([
            cv.Circle(translateX, translateY, radius * 0.05, paint=centerDotPaint),
            cv.Path([
                    cv.Path.MoveTo(
                        translateX,
                        translateY
                    ),
                    cv.Path.LineTo(
                        translateX + 0,
                        translateY + handWidth / 2
                    ),
                    cv.Path.LineTo(
                        translateX + handLength * 0.95,
                        translateY + handWidth / 2
                    ),
                    cv.Path.LineTo(
                        translateX + handLength,
                        translateY + 0
                    ),
                    cv.Path.Close()
                ],
                paint=handPaintStroke
            ),
            cv.Path([
                    cv.Path.MoveTo(
                        translateX,
                        translateY
                    ),
                    cv.Path.LineTo(
                        translateX + 0,
                        translateY - handWidth / 2
                    ),
                    cv.Path.LineTo(
                        translateX + handLength * 0.95,
                        translateY - handWidth / 2
                    ),
                    cv.Path.LineTo(
                        translateX + handLength,
                        translateY + 0
                    ),
                    cv.Path.Close()
                ],
                paint=handPaintFill
            ),
            cv.Circle(translateX, translateY, radius * 0.04, paint=centerCirclePaint),
        ],
        expand=1,
        rotate=ft.transform.Rotate(angle, alignment=ft.alignment.center),
        animate_rotation=ft.animation.Animation(300, ft.AnimationCurve.BOUNCE_OUT),
    )

    return hand


def Hands(handType: HandType, settings:dict, shape: HandShape, radius:float = 200, randomColor:bool = False):
    if shape == HandShape.ARROW:

        if handType == HandType.SECOND:
            return arrowHand(
                handType=HandType.SECOND,
                radius=radius,
                settings=settings,
                randomColor=randomColor
        )

        if handType == HandType.MINUTE:
            return arrowHand(
                    handType=HandType.MINUTE,
                    radius=radius,
                    settings=settings,
                    randomColor=randomColor
            )

        if handType == HandType.HOUR:
            return arrowHand(
                    handType=HandType.HOUR,
                    radius=radius,
                    settings=settings,
                    randomColor=randomColor
            )

    return None
