import flet as ft


def main(page: ft.Page):
    """
    Configura y ejecuta una aplicación de ejemplo con un NavigationRail personalizado.

    Args:
        page (ft.Page): La página principal de la aplicación.

    """
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended = True,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER,
                selected_icon=ft.icons.FAVORITE,
                label="Favorite",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Marked",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destionation:", e.control.selected_index),
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column(
                    [ft.Text("Body!")],
                    alignment=ft.MainAxisAlignment.START,
                    expand=True,
                ),
            ],
            expand=True,
        )
    )

# Inicia la aplicación
ft.app(target=main)
