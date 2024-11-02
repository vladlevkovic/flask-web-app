from flask import Flask
from routers.auth import user_bp
from models.base import create_db
from models.user import User
import binascii
import os


app = Flask(__name__)


def create_app():
    app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))
    app.register_blueprint(user_bp)
    return app

if __name__ == '__main__':
    create_db()
    app = create_app()
    app.run()
