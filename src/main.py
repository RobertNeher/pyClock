# import argparse
import io
import json
import time
from datetime import datetime

import flet as ft
import flet.canvas as cv

from math import pi

from clock_hands import clockHourHands, clockMinuteHands, clockSecondHands, handsSpindle, HandType
from random_color import random_Color
from digit_circle import digitCircle
from tick_circle import tickCircle
from clock_face import clockFace

def main(page: ft.Page) -> None:
    settings = json.load(io.open("assets/settings.json", "r", encoding="UTF-8"))["settings"]
    randomColor = settings["randomColor"]
    dateField = settings["dateField"]
    face = settings["clockFace"]
    secondsHand = settings["secondHand"]
    period = settings["updatePeriod"]
    radius = settings["radius"]
    colors = settings["colors"]

    backgroundColor = colors["clockFace"] if not randomColor else random_Color()

    clockFaceCanvas = clockFace(radius=radius, colors=colors, clockFace=face, randomColor=randomColor)

    clockFaceCanvas.shapes.extend(tickCircle(radius=radius, colors=colors, randomColor=randomColor))
    clockFaceCanvas.shapes.extend(digitCircle(radius=radius, colors=colors, randomColor=randomColor))

    page.window.width = 2.2 * radius
    page.window.height = 2.3 * radius

    face = ft.Container(
            alignment=ft.alignment.top_center,
            height = radius * 2,
            width = radius * 2,
            bgcolor=backgroundColor,
            padding=0,
            content=clockFaceCanvas,
    )

    secondHand = cv.Canvas(
        shapes=clockSecondHands(
            radius=radius,
            randomColor=randomColor,
            settings=settings
        ),
        rotate=ft.transform.Rotate(-pi/2),
        animate_rotation=ft.animation.Animation(0, ft.AnimationCurve.BOUNCE_OUT),
    )
    minuteHand = cv.Canvas(
        shapes=clockMinuteHands(
            radius=radius,
            randomColor=randomColor,
            settings=settings
        ),
        rotate=ft.transform.Rotate(-pi/2),
        animate_rotation=ft.animation.Animation(0, ft.AnimationCurve.BOUNCE_OUT),
    )
    hourHand = cv.Canvas(
        shapes=clockHourHands(
            radius=radius,
            randomColor=randomColor,
            settings=settings
        ),
        rotate=ft.transform.Rotate(-pi/2),
        animate_rotation=ft.animation.Animation(300, ft.AnimationCurve.BOUNCE_OUT),
    )

    centerPin = cv.Canvas(
        shapes=handsSpindle(
            radius=radius,
            settings=settings,
            randomColor=randomColor
        )
    )

    clockApp = ft.Stack(
        [face],
        alignment=ft.alignment.center
    )

    if settings["secondHand"]:
        clockApp.controls.extend([secondHand])

    clockApp.controls.extend([minuteHand, hourHand, centerPin])

    page.add(clockApp)

    # second = 0
    # minute = 0
    # hour = 0
    while True:
        second = datetime.now().second
        minute = datetime.now().minute
        hour = datetime.now().hour % 12

        if settings["secondHand"]:
            secondHand.rotate = ft.transform.Rotate((second * 2 * pi/60) - pi/2)

        minuteHand.rotate = ft.transform.Rotate(((minute + (1 * second/60)) * (2*pi)/60) - pi/2)
        hourHand.rotate = ft.transform.Rotate(((hour * 2 * pi/12) + (5 * minute/60) * 2 * pi/60) - pi/2)

        page.expand = 1
        page.update()

        # second += 1

        # if second > 60:
        #     second = 0
        #     minute += 1

        #     if minute > 60:
        #         minute = 0
        #         hour += 1

        #         if hour > 24:
        #             hour = 0
        

        time.sleep(1)

ft.app(main)
