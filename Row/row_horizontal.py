import flet as ft

def main(page: ft.Page):
    
    def items(count):
        """lista vacía de items, por el rango 1 hasta el valor que recive + 1 agregue los elementos a la lista como siguiendo los valores del contenedor y los devuelva"""
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.Text(value=str(i)),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.colors.AMBER_500,
                )
            )
        return items

    def row_with_alignment(align: ft.MainAxisAlignment):
        """crea una columna con un texto que describe la alineación y una fila con tres elementos alineados de acuerdo con el argumento de alineación proporcionado"""
        return ft.Column([
            ft.Text(str(align), size=16),
            ft.Container(
                content=ft.Row(items(3), alignment=align),
                bgcolor=ft.colors.AMBER_100,
            ),
        ])
    
    page.add(
        row_with_alignment(ft.MainAxisAlignment.START),
        row_with_alignment(ft.MainAxisAlignment.CENTER),
        row_with_alignment(ft.MainAxisAlignment.END),
        row_with_alignment(ft.MainAxisAlignment.SPACE_BETWEEN),
        row_with_alignment(ft.MainAxisAlignment.SPACE_AROUND),
        row_with_alignment(ft.MainAxisAlignment.SPACE_EVENLY),
    )

ft.app(target=main)