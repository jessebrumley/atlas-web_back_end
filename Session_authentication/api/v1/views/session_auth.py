#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ log a user in
    """
    # Check if form contains email
    email = request.form.get('email')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    # Check if form contains password
    password = request.form.get('password')
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    # Check if email is valid and in the database
    user = User.search({'email': email})
    if len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    # Check if the password is valid
    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    # Create a session ID, set it into a cookie, and set it on the
    # response object containing the authenticated user
    from api.v1.app import auth
    sesh_id = auth.create_session(user[0].id)
    response = jsonify(user[0].to_json())
    response.set_cookie(getenv('SESSION_NAME'), sesh_id)
    return response


@app_views.route(
    '/auth_session/logout/',
    methods=['DELETE'],
    strict_slashes=False)
def logout():
    """ logout method
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
