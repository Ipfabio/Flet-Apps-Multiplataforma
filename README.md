# Flet-Apps-Multiplataforma

Apps desarrolladas con Flutter en Python utilizando Flet

Flet es un framework relativamente nuevo que permite a los desarrolladores crear aplicaciones web, móviles y de escritorio en tiempo real en Python. Flet simplifica la arquitectura de las aplicaciones al permitir a los desarrolladores escribir una aplicación monolítica y stateful en Python, lo que les permite obtener una aplicación de página única (SPA) multiusuario y en tiempo real.

Flet Controls es una interfaz de usuario desarrollada en Flutter que permite a los desarrolladores manipular widgets de otro lenguaje, pero en Python. Flet UI está construido con Flutter, lo que hace que las aplicaciones tengan un aspecto profesional y puedan entregarse en cualquier plataforma

Toda la documentación esta en: https://flet.dev/docs/cli

# Testing Flet app on IOS y Android 

`flet run --ios counter.py` | `flet run --android counter.py`
Esto genera un código QR para descargar su aplicación y probarla en dispositivos móviles

# Packaging desktop app

`pip install pyinstaller`

`flet pack your_program.py`
