import flet as ft

def main(page: ft.Page):
    """Crea un ejemplo sencillo de NavigationBar en una aplicación Flet."""
    page.title = "NavitationBar Example"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon= ft.icons.EXPLORE, label="Explore"),
            ft.NavigationDestination(icon=ft.icons.COMMUTE_ROUNDED, label="Commute"),
            ft.NavigationDestination(icon=ft.icons.BOOKMARK_BORDER, selected_icon=ft.icons.BOOKMARK, label="Explore"),
        ]
    )
    page.add(ft.Text("Body!"))

ft.app(target=main)