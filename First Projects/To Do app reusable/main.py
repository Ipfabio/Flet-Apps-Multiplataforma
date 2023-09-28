import flet as ft
from to_do import TodoApp


def main(page: ft.Page):
    """
    Configura y ejecuta una aplicación de lista de tareas (ToDo).
    """
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # Create application instance
    todo = TodoApp()
    # app1 = TodoApp()
    # app2 = TodoApp()

    # add application's root control to the page
    page.add(todo)
    # page.add(app1, app2)


ft.app(target=main)
