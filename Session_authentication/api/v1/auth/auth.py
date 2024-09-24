#!/usr/bin/env python3
""" Authentication module
"""
from flask import request
from typing import List, TypeVar
import os

User = TypeVar('User')


class Auth:
    """ Auth class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required for a given path
        Args:
            path: The requested path
            excluded_paths: List of paths that do not require authentication
        Returns:
            bool: True if authentication is required, False otherwise
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        normalized_path = path.rstrip('/')

        for excluded_path in excluded_paths:
            if normalized_path == excluded_path.rstrip('/'):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header from the request
        Args:
            request: The Flask request object
        Returns:
            str: None, as we are not implementing this now
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> User:
        """ Retrieves the current user from the request
        Args:
            request: The Flask request object
        Returns:
            User: None, as we are not implementing this now
        """
        return None

    def session_cookie(self, request=None):
        """
        Retrieves the session cookie value from the request.

        Args:
            request: The Flask request object

        Returns:
            str: value of session cookie (_my_session_id), None if not found
        """
        if request is None:
            return None

        # Retrieve the cookie name from the environment variable SESSION_NAME
        cookie_name = os.getenv('SESSION_NAME', '_my_session_id')

        # Return the value of the session cookie if it exists
        return request.cookies.get(cookie_name, None)
