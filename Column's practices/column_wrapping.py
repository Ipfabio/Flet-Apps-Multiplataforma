import flet as ft

HEIGHT = 400

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
                    width=30,
                    height=30,
                    bgcolor=ft.colors.AMBER,
                    border_radius=ft.border_radius.all(5),
                )
            )
        return items
    
    def slider_change(e):
        """
        Actualiza el espaciado entre los contenedores basado en el valor del control deslizante.
        """
        col.height = float(e.control.value)
        col.update()
        
    width_slider = ft.Slider(
        min=0,
        max=HEIGHT,
        divisions=20,
        value=HEIGHT,
        label="{value}",
        width=500,
        on_change=slider_change,
    )
    
    col = ft.Column(
        wrap=True,
        spacing=10,
        run_spacing=10,
        controls=items(10),
        height=HEIGHT
    )
    
    page.add(ft.Column([ft.Text("Change the column width to see how child items wrap"), width_slider]), ft.Container(content=col, bgcolor=ft.colors.AMBER_100),)
    
ft.app(target=main)