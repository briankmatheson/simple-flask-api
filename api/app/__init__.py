from flask import Flask
from app.mod_static.controllers import response

def create_app():
    app = Flask(__name__)
    app.register_blueprint(response)
    return app


