import flet as ft

import io
import json

from moon_phase import moonPhase, moonPhaseOnDay


def main(page: ft.Page):
    settings = json.load(io.open("assets/settings.json", "r", encoding="UTF-8"))["settings"]
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.WHITE
    page.window.bgcolor = ft.Colors.WHITE60
    radius = settings["radius"]
    randomColor = settings["randomColor"]

    page.add(
        moonPhase(radius=radius, settings=settings, randomColor=randomColor)
    )

# if __name__ == "__main__":

ft.app(main)
