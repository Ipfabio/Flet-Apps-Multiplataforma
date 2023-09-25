import threading
import flet as ft

class State:
    i = 0

s = State()
sem = threading.Semaphore()

def main(page: ft.Page):
    """
    Configura una página con una columna desplazable que carga más contenido al desplazarse hacia abajo.
    """
    def on_scroll(e: ft.OnScrollEvent):
        """
        Maneja el evento de desplazamiento y carga más contenido cuando se desplaza hacia abajo.
        """
        if e.pixels >= e.max_scroll_extent - 100:
            if sem.acquire(blocking=False):
                try:
                    for i in range(0, 10):
                        cl.controls.append(ft.Text(f'Text line {s.i}', key=str(s.i)))
                        s.i += 1
                    cl.update()
                finally:
                    sem.release()
    
    cl = ft.Column(
        spacing=10,
        height=200,
        width=300,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=on_scroll,
    )
    
    for i in range(0, 50):
        cl.controls.append(ft.Text(f'Text line {s.i}', key=str(s.i)))
        s.i += 1
    
    page.add(ft.Container(cl, border=ft.border.all(1)))

ft.app(target= main)