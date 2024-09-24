#!/usr/bin/env python3
"""
Route module for the API
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os


@app.before_request
def handle_request():
    """
    Handles request authorization.

    Checks if the current path requires authentication
    """
    handled_paths = ['/api/v1/status/',
                     '/api/v1/unauthorized/',
                     '/api/v1/forbidden/']

    # Check if the current path requires authentication
    if auth is not None and auth.require_auth(request.path, handled_paths):
        # If authentication is required, check for the Authorization header
        if auth.authorization_header(request) is None:
            abort(401)

        # check if the user is authenticated
        if auth.current_user(request) is None:
            abort(403)

    # Allow unauthenticated access to /api/v1/status
    if request.path == '/api/v1/status/' and auth is not None:
        auth.handle_status_request(request)


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Handles 404 Not Found errors.

    Returns a JSON response with an "error" key set to "Not found".
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def not_authorized(error) -> str:
    """
    Handles 401 Unauthorized errors.

    Returns a JSON response with an "error" key set to "Unauthorized".
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def access_forbidden(error) -> str:
    """
    Handles 403 Forbidden errors.

    Returns a JSON response with an "error" key set to "Forbidden".
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    """
    Main execution block.

    Sets up and runs the Flask application based on environment variables.
    """
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
