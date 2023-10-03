from calculator import CalculatorApp
import flet as ft


def main(page: ft.Page):
    """
    Función principal para ejecutar la aplicación Calculadora.

    Args:
        page (ft.Page): La página de Flet a la que se agregará la aplicación.
    """
    page.title = "Calculator App"

    calc = CalculatorApp()

    page.add(calc)


ft.app(target=main)
