import flet as ft

def main(page: ft.Page):
    """
    Configura una página con contenedores numerados y un control deslizante para ajustar el espacio entre ellos.
    """   
    def items(count):
        """
        Crea y devuelve una lista de contenedores    cuadrados numerados del 1 al 'count'.
        """
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
    
    def spacing_slider_change(e):
        """
        Actualiza el espaciado entre los contenedores basado en el valor del control deslizante.
        """
        col.spacing = int(e.control.value)
        col.update()
        
    gap_slider = ft.Slider(
        min=0,
        max=100,
        divisions=10,
        value=0,
        label="{value}",
        width=500,
        on_change=spacing_slider_change,
    )
    
    col = ft.Column(spacing=0, controls=items(5))
    
    page.add(ft.Column([ft.Text("Spacing between items"), gap_slider]), col)
    
ft.app(target=main)