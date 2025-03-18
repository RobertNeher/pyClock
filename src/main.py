import io
import json
import time
from datetime import datetime

import flet as ft
import flet.canvas as cv

from math import pi

from clock_hands import arrowHand, spindle, HandType
from moon_phase import moonPhase
from random_color import random_Color
from hour_ring import hourRing
from tick_ring import tickRing
from clock_face import clockFace
from complications import weekDay, dateWindow

def main(page: ft.Page) -> None:
    settings = json.load(io.open("assets/settings.json", "r", encoding="UTF-8"))["settings"]
    randomColor = settings["randomColor"]
    face = settings["clockFace"]
    radius = settings["radius"]
    colors = settings["colors"]
    complications = settings["complications"]
    digitTurn = settings["digitTurn"]

    page.window.width = 2.3 * radius
    page.window.height = 2.3 * radius
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    backgroundColor = colors["clockFace"] if not randomColor else random_Color()

    clockFaceCanvas = clockFace(radius=radius, colors=colors, clockFace=face, randomColor=randomColor)

    clockFaceCanvas.shapes.extend(tickRing(radius=radius, colors=colors, randomColor=randomColor))
    clockFaceCanvas.shapes.extend(hourRing(radius=radius, colors=colors, digitTurn=digitTurn, randomColor=randomColor))

    clock_Face = ft.Container(
            alignment=ft.alignment.top_left,
            height = radius * 2,
            width = radius * 2,
            bgcolor=ft.Colors.TRANSPARENT if not face else backgroundColor,
            padding=0,
            content=clockFaceCanvas,
    )

    secondHand = cv.Canvas(
        shapes=arrowHand(
            handType=HandType.SECOND,
            radius=radius,
            randomColor=randomColor,
            settings=settings
        ),
        rotate=ft.transform.Rotate(-pi/2),
        animate_rotation=ft.animation.Animation(0, ft.AnimationCurve.BOUNCE_IN_OUT),
    )
    minuteHand = cv.Canvas(
        shapes=arrowHand(
            handType=HandType.MINUTE,
            radius=radius,
            randomColor=randomColor,
            settings=settings
        ),
        rotate=ft.transform.Rotate(-pi/2),
        animate_rotation=ft.animation.Animation(500, ft.AnimationCurve.BOUNCE_IN_OUT),
    )
    hourHand = cv.Canvas(
        shapes=arrowHand(
            handType=HandType.HOUR,
            radius=radius,
            randomColor=randomColor,
            settings=settings
        ),
        rotate=ft.transform.Rotate(-pi/2),
        animate_rotation=ft.animation.Animation(500, ft.AnimationCurve.BOUNCE_IN_OUT),
    )

    centerPin = cv.Canvas(
        shapes=spindle(
            radius=radius,
            settings=settings,
            randomColor=randomColor
        ),
    )

    date_Window = cv.Canvas(
        shapes=dateWindow(radius=radius, settings=settings, randomColor=randomColor),
    )

    week_Day = cv.Canvas(
        shapes=weekDay(radius=radius, settings=settings, randomColor=randomColor),
    )
    clockApp = ft.Stack(
        [date_Window, clock_Face],
        alignment=ft.alignment.center
    )

    clockApp.controls.extend([hourHand, minuteHand])
    clockApp.controls.append(centerPin)

    if settings["secondHand"]:
        clockApp.controls.append(secondHand)

    if complications["dateWindow"]:
        clockApp.controls.append(date_Window)

    if complications["weekDay"]:
        clockApp.controls.append(week_Day)

    if complications["moonPhase"]:
        clockApp.controls.append(moonPhase(radius=radius, settings=settings, randomColor=randomColor))

    page.add(clockApp)
    page.expand = 1

    if not face:
        page.window.bgcolor = ft.Colors.TRANSPARENT
        page.bgcolor = ft.Colors.TRANSPARENT

    while True:
        second = datetime.now().second
        minute = datetime.now().minute
        hour = datetime.now().hour % 12

        if settings["secondHand"]:
            secondHand.rotate = ft.transform.Rotate((second * 2 * pi/60) - pi/2)

        if settings["smoothHands"]:
            minuteHand.rotate = ft.transform.Rotate((minute + (1 * second/60)) * (2*pi/60) - pi/2)
            hourHand.rotate = ft.transform.Rotate(((hour * 2 * pi/12) + (5 * minute/60) * 2 * pi/60) - pi/2)
        else:
            minuteHand.rotate = ft.transform.Rotate((minute * 2*pi/60) - pi/2)
            hourHand.rotate = ft.transform.Rotate((hour * 2 * pi/12) - pi/2)

        page.update()

        time.sleep(settings["updatePeriod"])

ft.app(main)
