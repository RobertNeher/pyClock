import io
import json
import math

import flet as ft
import flet.canvas as cv

# from src.clock_face import clockFace

def main(page: ft.Page) -> None:
    settings = json.load(io.open("assets/settings.json", "r", encoding="UTF-8"))["settings"]

    randomColor = settings["randomColor"]
    dateField = settings["dateField"]
    face = settings["clockFace"]
    secondsHand = settings["secondHand"]
    period = settings["updatePeriod"]
    radius = settings["radius"]
    colors = settings["colors"]
    handSettings = settings["hands"]
    
    centerDotPaint = ft.Paint(
        style=ft.PaintingStyle.FILL,
        color= colors["centerDot"] # random_Color() if randomColor else colors["centerDot"]
    )
    centerCirclePaint = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=3,
        color= colors["centerTop"] # random_Color() if randomColor else colors["centerDot"]
    )
    secondHandPaintStroke = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=2,
        color= colors["secondHand"] # random_Color() if randomColor else colors["secondHand"]
    )
    secondHandPaintFill = ft.Paint(
        style=ft.PaintingStyle.FILL,
        stroke_width=2,
        color= colors["secondHand"] # random_Color() if randomColor else colors["secondHand"]
    )

    translateX = radius
    translateY = radius

    roundedHand = cv.Canvas(
            [
                cv.Arc(
                    x= translateX + 0,
                    y= translateY - handSettings["secondHandWidth"],
                    height=handSettings["secondHandWidth"],
                    width=handSettings["secondHandWidth"],
                    start_angle=math.pi / 2.0,
                    sweep_angle=math.pi / 2.0,
                    use_center=False,
                    paint=secondHandPaintFill
                ),
                cv.Path(elements=[
                        cv.Path.MoveTo(
                              translateX,
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
            ],
            width=float("inf"),
            expand=True,
    )
    page.window.width = 2.2 * radius
    page.window.height = 2.3 * radius
    page.add(ft.Container(
        alignment=ft.alignment.top_center,
        height = radius * 2,
        width = radius * 2,
        bgcolor=ft.Colors.TRANSPARENT,
        padding=10,
        content=roundedHand
    ))

# if __name__ == "__main__":
ft.app(main)

    # arrowHand = cv.Canvas(
    #         [
    #          -->cv.Circle(translateX, translateY, radius * 0.05, paint=centerDotPaint),
    #             cv.Path(elements=[
    #                     cv.Path.MoveTo(
    #                           translateX,
    #                           translateY
    #                     ),
    #                     cv.Path.LineTo(
    #                         translateX + 0,
    #                         translateY + handSettings["secondHandWidth"] / 2.0
    #                     ),
    #                     cv.Path.LineTo(
    #                         translateX + radius * handSettings["secondHandFactor"] * 0.9,
    #                         translateY + handSettings["secondHandWidth"] / 2.0
    #                     ),
    #                     cv.Path.LineTo(
    #                         translateX + radius * handSettings["secondHandFactor"],
    #                         translateY + 0
    #                     )
    #                 ],
    #                 paint=secondHandPaintStroke
    #             ),
    #             cv.Path(elements=[
    #                     cv.Path.MoveTo(
    #                           translateX,
    #                           translateY
    #                     ),
    #                     cv.Path.LineTo(
    #                         translateX + 0,
    #                         translateY - handSettings["secondHandWidth"] / 2.0
    #                     ),
    #                     cv.Path.LineTo(
    #                         translateX + radius * handSettings["secondHandFactor"] * 0.9,
    #                         translateY - handSettings["secondHandWidth"] / 2.0
    #                     ),
    #                     cv.Path.LineTo(
    #                         translateX + radius * handSettings["secondHandFactor"],
    #                         translateY + 0
    #                     )
    #                 ],
    #                 paint=secondHandPaintFill
    #             ),    
    #          -->cv.Circle(translateX, translateY, radius * 0.04, paint=centerCirclePaint),
    #         ],
    #         width=float("inf"),
    #         expand=True,
    # )

