import flet as ft

class TodoApp(ft.UserControl):
    """
    Aplicación de lista de tareas simple.
    """
    def build(self):
        """
        Construye la interfaz de usuario de la aplicaión
        """
        self.new_task = ft.TextField(hint_text="Que hay que hacer?", expand=True)
        self.tasks = ft.Column()
        
        # Applcations's root control (i.e. "view") containing all other controls
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[self.new_task,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks,
            ],
        )
        
    def add_clicked(self, e):
        """
        Maneja el evento de clic en el botón "Agregar tarea" y agrega una nueva tarea
        """
        self.tasks.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()