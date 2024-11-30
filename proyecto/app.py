from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Ruta para la página de control
@app.route('/')
def control():
    return render_template('control.html')

# Ruta para la página de visualización
@app.route('/display')
def display():
    return render_template('display.html')

# Manejo del evento de selección de video desde el control
@socketio.on('select_video')
def handle_video_selection(data):
    # Emitimos el evento para actualizar el video en la página de visualización
    emit('update_video', {'video': data['video']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
