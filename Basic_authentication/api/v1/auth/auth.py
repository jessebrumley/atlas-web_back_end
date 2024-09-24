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
            bool: False, as we are not implementing this now
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header from the request
        Args:
            request: The Flask request object
        Returns:
            str: None, as we are not implementing this now
        """
        return None

    def current_user(self, request=None) -> User:
        """ Retrieves the current user from the request
        Args:
            request: The Flask request object
        Returns:
            User: None, as we are not implementing this now
        """
        return None
