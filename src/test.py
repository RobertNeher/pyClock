import flet as ft
import flet.canvas as cv

from datetime import datetime
from math import pi

from arc_text import arcText
import sys

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.bgcolor = ft.Colors.WHITE54
    page.add(
        cv.Canvas(
            shapes=arcText(text="Robert Neher", radius=100, colors={}, randomColor=True),
        )
    )

# if __name__ == "__main__":

ft.app(main)
