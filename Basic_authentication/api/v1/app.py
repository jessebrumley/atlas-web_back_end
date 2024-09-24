#!/usr/bin/env python3
"""
Route module for the API.
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os

auth = None
auth_type = os.getenv('AUTH_TYPE')
if auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()

app = Flask(__name__)

# Register the blueprint here to ensure it's only done once
app.register_blueprint(app_views)

CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.before_request
def handle_request():
    """Handle request authorization."""
    handled_paths = ['/api/v1/status',
                     '/api/v1/unauthorized',
                     '/api/v1/forbidden']
    if auth is not None:
        if auth.require_auth(request.path, handled_paths):
            if auth.authorization_header(request) is None:
                abort(401)
            if auth.current_user(request) is None:
                abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """Not found handler.

    Args:
        error: The error object.

    Returns:
        A JSON response with a 404 status.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def not_authorized(error) -> str:
    """Not authorized handler.

    Args:
        error: The error object.

    Returns:
        A JSON response with a 401 status.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def access_forbidden(error) -> str:
    """Forbidden route handler.

    Args:
        error: The error object.

    Returns:
        A JSON response with a 403 status.
    """
    return jsonify({"error": "Forbidden"}), 403


@app_views.route('/api/v1/status', methods=['GET'])
def status():
    """Returns the status of the API.

    Returns:
        A JSON response with the status of the API.
    """
    return jsonify({"status": "OK"}), 200


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
