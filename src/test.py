import flet as ft


def main(page: ft.Page):
    def adaptRadius(e: ft.WindowEvent) -> None:
        radius = 0

        if e.control.height > (2 * radius) or e.control.width > (2 * radius):
            if e.control.height > e.control.width:
                radius = e.control.height / 2
                page.window.width = e.control.height
            else:
                radius = e.control.width / 2
                page.window.height = e.control.width

        page.expand = 1
        page.update()

    radius = 100
    c = ft.Container(
         width = 200,
         height = 300,
         bgcolor=ft.Colors.TRANSPARENT
    )
    page.bgcolor = ft.Colors.TRANSPARENT
    page.window.bgcolor = ft.Colors.TRANSPARENT
    page.window.width = 200,
    page.window.height = 300,
    page.on_resized=adaptRadius
    page.add(
         c,
         ft.Text(radius))
    page.expand = 1
    page.update()

ft.app(main)
