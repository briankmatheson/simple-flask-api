from flask import Blueprint, request
from flask_api import status
from psycopg2 import connect
import json 

blueprint = Blueprint('blueprint', __name__)
db = connect(host="db-simple-flask-app-postgresql", 
             dbname="simple_flask_app",
             user="postgres", 
             password="rX0l6HqO2p")

@blueprint.route('/ping')
@blueprint.route('/')
def ping():
    return 'pong!'

@blueprint.route('/hello')
def hello_world():
    return 'Hello, World!'

@blueprint.route('/echo', methods=["POST"])
def echo():
    uuid = request.form['uuid']
    return(uuid + "\n")

@blueprint.route('/add', methods=["POST"])
def add():
    uuid = request.form['uuid']
    cur = db.cursor()
    query = "INSERT INTO uuids (uuid) VALUES (%s);"
    cur.execute(query, [uuid])
    return "okay\n", status.HTTP_201_CREATED

@blueprint.route('/get', methods=["GET"])
def get():
    cur = db.cursor()
    query = "SELECT * from uuids;"
    cur.execute(query)
    resp = json.dumps(cur.fetchall())
    return(resp)
