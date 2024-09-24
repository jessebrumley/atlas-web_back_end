#!/usr/bin/env python3
""" Session Authentication Module
"""
from api.v1.auth.auth import Auth
from models.user import User
from flask import request
import uuid


class SessionAuth(Auth):
    """ Session Authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for a user_id
        Args:
            user_id: The ID of the user
        Returns:
            Session ID or None
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Retrieves the User ID based on a Session ID
        Args:
            session_id: The Session ID
        Returns:
            User ID or None
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        """ Retrieves the current User based on the session cookie
        Args:
            request: The Flask request object
        Returns:
            User instance or None
        """
        if request is None:
            return None

        # Retrieve the session ID from the cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        # Get the User ID using the session ID
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        # Retrieve the User instance from the database
        return User.get(user_id)

    def session_cookie(self, request=None):
        """ Retrieves the session cookie value from the request
        Args:
            request: The Flask request object
        Returns:
            Cookie value or None
        """
        if request is None:
            return None
        return request.cookies.get(os.getenv('SESSION_NAME', '_my_session_id'))
