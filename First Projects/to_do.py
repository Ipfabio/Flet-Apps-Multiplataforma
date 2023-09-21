import flet as ft

def main(page: ft.Page):
    
    def add_clicked(e):
        """Agrega una casilla de verificación con una etiqueta al control de vista de tareas cuando se llama. Luego, borra el valor del campo de entrada `new_task` y actualiza la vista."""
        tasks_view.controls.append(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        view.update()
    
    # Creamos un campo de texto y dejamos en true la propiedad para que se expanda horizontalmente de ser necesario
    new_task = ft.TextField(hint_text="Que tienes que hacer?", expand=True)
    
    # Utilizamos ésta columna para mostrar la lista de tareas
    tasks_view = ft.Column()
    
    # Control de columna, actúa como contendor principal de la interfaz
    view = ft.Column(
        width=600, # Establece ancho en 600 unidades
        controls=[ #definimos los elementos de la interfaz
            ft.Row( # Control de fila, contenedor de elementos relacionados 
                controls=[
                    new_task, # Campo de texto
                    # Botón flotante para agregar tareas llamando a la función `add_clicked`
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked),
                ],
            ),
            tasks_view, # Columna para mostrar la lista de tareas
        ],
    )
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Centrado horizontalmente dentro de la página
    page.add(view) # Agregamos todo lo que hicimos

ft.app(target= main)