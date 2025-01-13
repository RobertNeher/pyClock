from math import pi
import time
import flet as ft
import flet.canvas as cv

def main(page: ft.Page):

    radius = 250
    handWidth = 20
    handLength = radius * 0.95
    translateX = 0
    translateY = radius - handWidth
    stroke_paint = ft.Paint(style=ft.PaintingStyle.STROKE)
    fill_paint = ft.Paint(style=ft.PaintingStyle.FILL)

    hand = cv.Canvas(
        [
            # cv.Circle(translateX, translateY, radius * 0.05, paint=fill_paint),
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
            paint=fill_paint
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
                paint=stroke_paint
            ),
            # cv.Circle(translateX, translateY, radius * 0.04, paint=stroke_paint),
        ],
        # width=float("inf"),
        expand=1,
        rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
        animate_rotation=ft.animation.Animation(300, ft.AnimationCurve.BOUNCE_OUT),
    )

    page.window.height = 2 * radius
    page.window.width = 2 * radius
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        hand
    )
    page.expand=1

    angle = -pi/2

    while angle <= 2*pi:
        hand.rotate.angle = angle
        page.update()
        time.sleep(0.5)
        angle += 2*pi/60


ft.app(main)
