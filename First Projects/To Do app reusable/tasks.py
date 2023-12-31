import flet as ft


class Task(ft.UserControl):
    """
    Representa una tarea en la lista de tareas.

    Args:
        task_name (str): El nombre de la tarea.
        task_status_change (function): Maneja el cambio de estado (completado o no) de la tarea.
        task_delete (function): Una función que se llama al eliminar la tarea.

    Methods:
        edit_clicked: Maneja el evento de edición de la tarea.
        save_clicked: Maneja el evento de guardado de la tarea editada.
        delete_clicked: Maneja el evento de eliminación de la tarea.
    """

    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

    def build(self):
        # Construye la interfaz de usuario para representar una tarea de la lista
        self.display_task = ft.Checkbox(
            value=False, label=self.task_name, on_change=self.status_change
        )
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        # Maneja el evento de edición de la tarea.
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        # Maneja el evento de guardado de la tarea editada.
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_change(self, e):
        # Maneja el cambio de estado (completo o no) de la tarea.
        self.completed = self.display_task.value
        self.task_status_change(self)

    def delete_clicked(self, e):
        # Maneja el evento de eliminación de la tarea.
        self.task_delete(self)
