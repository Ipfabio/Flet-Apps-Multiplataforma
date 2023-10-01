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
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="all"),
                ft.Tab(text="active"),
                ft.Tab(text="completed"),
            ],
        )

        self.items_left = ft.Text("0 items left")

        # Applcations's root control (i.e. "view") containing all other controls
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    [ft.Text(value="Todos", style="headlineMedium")],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
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
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                self.items_left,
                                ft.OutlinedButton(
                                    text="Clear completed", on_click=self.clear_clicked
                                ),
                            ],
                        ),
                    ],
                ),
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

    def clear_clicked(self, e):
        """
        Elimina las tareas completadas al hacer clic en "Limpiar completadas".
        """
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)

    def update(self):
        """
        Actualiza la visibilidad de las tareas según el estado seleccionado (todos, activos, completados).
        """
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "all"
                or (status == "active" and task.completed == False)
                or (status == "completed" and task.completed)
            )
            if not task.completed:
                count += 1
            self.items_left.value = f"{count} active item(s) left"
        super().update()

    def task_status_change(self, e):
        """
        Maneja el cambio de estado de una tarea y llama a `update`.
        """
        self.update()

    def tabs_changed(self, e):
        """
        Maneja el cambio de pestañas (todos, activos, completados) y llama a `update`.
        """
        self.update()

    def task_delete(self, task):
        """
        Elimina una tarea de la lista y llama a `update`.
        """
        self.tasks.controls.remove(task)
        self.update()
