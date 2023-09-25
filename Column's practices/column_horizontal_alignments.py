import flet as ft

def main(page: ft.Page):
    """
    Configura una página con varias columnas alineadas horizontalmente y ajusta su espaciado.
    """
    def items(count):
        """
        Crea y devuelve una lista de contenedores cuadrados numerados del 1 al 'count'."""
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
    
    def column_with_horiz_aligment(align:ft.MainAxisAlignment):
        """
        Crea y devuelve una columna con elementos alineados horizontalmente según 'align'.
        """
        return ft.Column([
            ft.Text(str(align), size=16),
            ft.Container(
                content=ft.Column(items(3),alignment=ft.MainAxisAlignment.START, horizontal_alignment = align,),
                bgcolor= ft.colors.AMBER_100,
                width=100,
            ),
        ])
        
    page.add(
        ft.Row([
            column_with_horiz_aligment(ft.CrossAxisAlignment.START),
            column_with_horiz_aligment(ft.CrossAxisAlignment.CENTER),
            column_with_horiz_aligment(ft.CrossAxisAlignment.END),
        ],
            spacing=30,
            alignment=ft.MainAxisAlignment.START,
        )
    )
    
ft.app(target=main)