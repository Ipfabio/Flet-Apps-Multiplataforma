import flet as ft


class CalculatorApp(ft.UserControl):
    """
    Representa una aplicación de calculadora simple con una interfaz de usuario de Flet.
    Esta clase define la estructura y el comportamiento de la aplicación calculadora.
    """

    def build(self):
        """Crea la interfaz de usuario de la aplicación calculadora."""
        self.reset()

        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=20)

        return ft.Container(
            # El contenedor raíz de la aplicación calculadora.
            width=350,  # 300 queda mejor
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.result], alignment="end"),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="AC",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="AC",
                            ),
                            ft.ElevatedButton(
                                text="+/-",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="+/-",
                            ),
                            ft.ElevatedButton(
                                text="%",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="%",
                            ),
                            ft.ElevatedButton(
                                text="/",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="/",
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
                                on_click=self.button_clicked,
                                data="7",
                            ),
                            ft.ElevatedButton(
                                text="8",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="8",
                            ),
                            ft.ElevatedButton(
                                text="9",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="9",
                            ),
                            ft.ElevatedButton(
                                text="*",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="*",
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
                                on_click=self.button_clicked,
                                data="4",
                            ),
                            ft.ElevatedButton(
                                text="5",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="5",
                            ),
                            ft.ElevatedButton(
                                text="6",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="6",
                            ),
                            ft.ElevatedButton(
                                text="-",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="-",
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
                                on_click=self.button_clicked,
                                data="1",
                            ),
                            ft.ElevatedButton(
                                text="2",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="2",
                            ),
                            ft.ElevatedButton(
                                text="3",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="3",
                            ),
                            ft.ElevatedButton(
                                text="+",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="+",
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
                                on_click=self.button_clicked,
                                data="0",
                            ),
                            ft.ElevatedButton(
                                text=".",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data=".",
                            ),
                            ft.ElevatedButton(
                                text="=",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="=",
                            ),
                        ]
                    ),
                ]
            ),
        )

    def button_clicked(self, e):
        data = e.control.data
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand == True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        elif data in ("+", "-", "*", "/"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True

        elif data in ("="):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()

        elif data in ("%"):
            self.result.value = float(self.result.value) / 100
            self.reset()

        elif data in ("+/-"):
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)
                # Version sugerida self.result.value = str(-float(self.result.value))

            elif float(self.result.value) < 0:
                self.result.value = str(
                    self.format_number(abs(float(self.result.value)))
                )
                self.update()

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):
        if operator == "+":
            return self.format_number(operand1 + operand2)
        elif operator == "-":
            return self.format_number(operand1 - operand2)
        elif operator == "*":
            return self.format_number(operand1 * operand2)
        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


""" 
El código define una clase CalculatorApp que representa una aplicación de calculadora simple
con una interfaz de usuario Flet. El método de compilación construye la interfaz de usuario de la aplicación.
Configura el diseño, los botones y otros elementos de la interfaz de usuario para la calculadora.
"""
