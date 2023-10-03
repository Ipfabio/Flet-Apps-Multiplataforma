import flet as ft


class CalculatorApp(ft.UserControl):
    """
    Representa una aplicación de calculadora simple con una interfaz de usuario de Flet.
    Esta clase define la estructura y el comportamiento de la aplicación calculadora.
    """

    def build(self):
        """Crea la interfaz de usuario de la aplicación calculadora."""
        result = ft.Text(value="0", color=ft.colors.WHITE, size=20)

        return ft.Container(
        # El contenedor raíz de la aplicación calculadora.
            width=350,  # 300 queda mejor
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[result], alignment="end"),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="AC",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="+/-",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="%",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="/",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="7",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="8",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="9",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="*",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="4",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="5",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="6",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="-",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="1",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="2",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="3",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="+",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="0",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=2,
                            ),
                            ft.ElevatedButton(
                                text=".",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="=",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                ]
            ),
        )

""" 
El código define una clase CalculatorApp que representa una aplicación de calculadora simple
con una interfaz de usuario Flet. El método de compilación construye la interfaz de usuario de la aplicación.
Configura el diseño, los botones y otros elementos de la interfaz de usuario para la calculadora.
"""