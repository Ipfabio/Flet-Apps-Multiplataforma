import flet as ft


def main(page: ft.Page):
    """
    Configura y ejecuta una aplicación de ejemplo con una AppBar personalizada y controles interactivos.

    Args:
        page (ft.Page): La página principal de la aplicación.

    """
    def check_item_clicked(e):
        """
        Maneja el evento de clic en un elemento de menú emergente.
        Cambia el estado de marcado o desmarcado del elemento y actualiza la página.

        Args:
            e (ft.Event): El evento de clic.

        """
        e.control.checked = not e.control.checked
        page.update()

    # Configuración de la AppBar personalizada
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example"),
        center_title= False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # Divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    # Agrega un control de texto al cuerpo de la página
    page.add(ft.Text("Body!"))

# Inicia la aplicación
ft.app(target=main)
