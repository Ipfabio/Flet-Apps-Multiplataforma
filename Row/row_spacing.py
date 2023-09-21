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
                    bgcolor=ft.colors.AMBER,
                    border_radius=ft.border_radius.all(5),
                )
            )
        return items

    def gap_slider_change(e):
        """Cambia el espaciado por el numero que le llega y actualiza row"""
        row.spacing = int(e.control.value)
        row.update()
    

    """Declaramos el valor minimo del slider en 0 y max en 50, comenzando en 0 (value) y que diga casa vez que lo movemos en cual estamos (label) y que al clickear se ejecute la función gap_slider_change"""
    gap_slider = ft.Slider( 
        min=0,
        max=50,
        divisions=50,
        value=0,
        label="{value}",
        on_change=gap_slider_change,
    )

    # espaciado 0, elementos del 1 al 10
    row = ft.Row(spacing=0, controls=items(10))
    
    # gap_slider es la barra que se desliza
    page.add(ft.Column([ft.Text("Spacing between items"), gap_slider]), row)

ft.app(target=main)