import flet as ft

def main(page: ft.Page):
    """Agrega a la página como texto el 'Hello World!'"""
    page.add(ft.Text(value="Hello, World!"))

ft.app(target= main)