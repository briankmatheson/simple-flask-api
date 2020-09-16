from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/ping')
    @app.route('/')
    def ping():
        return 'ack!'

    @app.route('/hello')
    def hello_world():
        return 'Hello, World!'

    return app

