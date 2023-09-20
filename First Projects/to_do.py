import flet as ft

def main(page: ft.Page):
    
    new_task = ft.TextField(hint_text="Whats need to be done?")
    
    def add_clcked(e):
        """Agrega a la página un checkbox con el label del valor de 'new_task'
        y actualiza la página"""
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()        
    # Agrega a la página, la nueva tarea y un botón de acción flotante y declaramos que al clickear se ejecute la función
    page.add(new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clcked))

ft.app(target= main)