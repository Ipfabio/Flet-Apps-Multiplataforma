import flet as ft

def main(page: ft.Page):
    def items(count):
        """
        Genera una lista de contenedores rectangulars con números dentro.

        Args:
            count (int): La cantidad de elementos en la lista.

        Returns:
            List[ft.Container]: Una lista de contenedores con números.

        Example:
            items(3) devuelve una lista con 3 contenedores numerados.
            """
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
    
    def row_with_vertical_alignment(align: ft.CrossAxisAlignment):
        """
    Crea una columna con un texto descriptivo y una fila alineada verticalmente según el valor de 'align'.

    Args:
        align (ft.CrossAxisAlignment): La alineación vertical de la fila ('ft.CrossAxisAlignment').

    Returns:
        ft.Column: Una columna con el texto y la fila alineada verticalmente.

    Example:
        row_with_vertical_alignment(ft.CrossAxisAlignment.center) para alinear elementos en la fila al centro.
        """
        return ft.Column([
            ft.Text(str(align), size=16),
            ft.Container(
                content=ft.Row(items(3), vertical_alignment=align),
                bgcolor= ft.colors.AMBER_100,
                height=150,
            )
        ])
        
    page.add(
        row_with_vertical_alignment(ft.CrossAxisAlignment.START),
        row_with_vertical_alignment(ft.CrossAxisAlignment.CENTER),
        row_with_vertical_alignment(ft.CrossAxisAlignment.END),
    )


ft.app(target=main)