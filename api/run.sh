#!/bin/sh
gunicorn --worker-class gevent -w 4 -b 0.0.0.0:8080 "app:create_app()"
