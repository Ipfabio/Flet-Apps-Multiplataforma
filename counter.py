import flet as ft

def main(page: ft.Page):
    # Lo declaramos como variable para poder trabajar con él desde las funciones
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)
    
    def minus(e):
        """Accedemos al valor, lo transformamos a int y le restamos 1"""
        txt_number.value = str(int(txt_number.value) - 1)
        txt_number.update()
    
    def plus(e):
        """Accedemos al valor, lo transformamos a int y le sumamos 1"""
        txt_number.value = str(int(txt_number.value) + 1)
        txt_number.update()
    
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus),
            ]
        )
    )

ft.app(main)