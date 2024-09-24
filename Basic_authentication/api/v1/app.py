#!/usr/bin/env python3
"""
Functions:
- before_request_handler(): Checks authorization before requests.
- not_found(error): Returns a 404 error message.
- unauthorized(error): Returns a 401 error message.
- forbidden(error): Returns a 403 error message.
"""
from os import getenv
from api.v1.auth.auth import Auth
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None

auth_type = os.getenv('AUTH_TYPE')

if auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    auth = Auth()


@app.before_request
def before_request_handler():
    """ Authorizes requests before processing.
    """
    if auth is None:
        return

    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/'
    ]

    if request.path in excluded_paths:
        return

    if request.path not in excluded_paths and \
            auth.require_auth(request.path, excluded_paths):
        if auth.authorization_header(request) is None:
            abort(401)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Handles 404 errors.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Handles 401 errors.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Handles 403 errors.
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
