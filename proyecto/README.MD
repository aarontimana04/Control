# Control de Videos en Páginas Separadas

Este proyecto consiste en una aplicación web simple creada con Flask y Flask-SocketIO. La aplicación permite seleccionar un video desde una página y redirige a otra página donde se reproduce el video seleccionado.

## Requisitos

- Python 3.x
- pip install (gestor de paquetes de Python)

## Instalación

1. **Clona el repositorio** o descarga los archivos del proyecto.
2. **Crea un entorno virtual** (opcional pero recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Linux/macOS
   venv\Scripts\activate     # En Windows
3. **Instala los requerimientos**
pip3 install -r requirements.txt
4. **Ejecuta la aplicacion**
python3 app.py
4. **Accede a:**
- http://127.0.0.1:5000 (control)
- http://127.0.0.1:5000/display (videos)