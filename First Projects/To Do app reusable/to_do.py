import flet as ft
from tasks import Task


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
        
        self.filter = ft.Tabs(
            selected_index=0,
            on_change= self.tabs_changed,
            tabs=[ft.Tab(text="all"), ft.Tab(text="active"), ft.Tab(text="completed"),]
        )
        

        # Applcations's root control (i.e. "view") containing all other controls
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, on_click=self.add_clicked
                        ),
                    ],
                ),
                ft.Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                    ]
                )
            ],
        )

    def add_clicked(self, e):
        """
        Maneja el evento de clic en el botón "Agregar tarea" y agrega una nueva tarea
        """
        task = Task(self.new_task.value, self.task_status_change, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()
        
    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = (
                status == "all"
                or (status == "active" and task.completed == False)
                or (status == "completed" and task.completed)
            )
        super().update()
    
    def task_status_change(self, e):
        self.update()
    
    def tabs_changed(self, e):
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()
