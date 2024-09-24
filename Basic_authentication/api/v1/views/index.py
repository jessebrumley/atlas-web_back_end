#!/usr/bin/env python3
""" Index Views Module
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ Endpoint to check API status
    Returns:
      - A JSON object with the API's status.
    """
    return jsonify({"status": "OK"})


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """ Route for unauthorized access
    """
    abort(401)


@app_views.route('/forbidden/', methods=['GET'], strict_slashes=False)
def forbidden_route():
    """ Route for forbidden access
    """
    abort(403)


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ Endpoint to retrieve statistics
    Returns:
      - A JSON object containing counts of various objects.
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)
