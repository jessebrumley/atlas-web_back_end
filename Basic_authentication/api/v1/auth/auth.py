#!/usr/bin/env python3
""" Authentication module
"""
from flask import request
from typing import List, TypeVar

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
        # Return True if path is None
        if path is None:
            return True

        # Return True if excluded_paths is None or empty
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize the path to remove trailing slashes for comparison
        normalized_path = path.rstrip('/')

        # Check if the normalized path is in excluded_paths
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
