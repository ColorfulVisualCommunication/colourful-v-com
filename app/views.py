# app/routes.py
from flask_socketio import emit, join_room, leave_room
from app import socketio

@socketio.on('send_message')
def handle_message(data):
    emit('receive_message', data, broadcast=True)
