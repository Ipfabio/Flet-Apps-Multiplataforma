import flet as ft

def main(page: ft.Page):
    
    # Titulo de la pagina
    page.title = "Mi contador con Flet"
    # Alineción general
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
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
            ],
            # Le decimos que se alinee al centro
            alignment= ft.MainAxisAlignment.CENTER
        )
    )
    

ft.app(main)

"""
Podemos activar el 'Hot reload' utilizando el comando en la consola 
-> flet run main.py -r
Hara que se actualice tanto app de escritorio como en browser los valores
"""