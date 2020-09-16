from flask import Blueprint

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/ping')
@blueprint.route('/')
def ping():
    return 'ack!'

@blueprint.route('/hello')
def hello_world():
    return 'Hello, World!'

