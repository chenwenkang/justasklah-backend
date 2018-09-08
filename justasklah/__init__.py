import os

from flask import Flask
from flask_socketio import SocketIO
from .db import __init_db
from .api import api_bp, MessageSocket


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    __init_db(app)
    return app


def create_socketio(app):
    socketio = SocketIO(app)
    socketio.on_namespace(MessageSocket('/message/socket'))
    return socketio
