import flet as ft

def main(page: ft.Page):
    """Añade a la 'Hoja' el texto de Hola, Flet!"""
    page.add(ft.Text("Hola, Flet!"))
    
"""Generamos la app y le pasamos el nombre de la función, en este caso -> main"""
# Asi se genera una aplicación nativa
ft.app(main)

# Si agregamos -> view=ft.Web_Browser lo genera en un navegador
# ft.app(main, view=ft.WEB_BROWSER)