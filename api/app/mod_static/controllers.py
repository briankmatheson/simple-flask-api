from flask import Blueprint

response = Blueprint('ping', __name__)


@response.route('/ping')
@response.route('/')
def ping():
    return 'ack!'

@response.route('/hello')
def hello_world():
    return 'Hello, World!'

