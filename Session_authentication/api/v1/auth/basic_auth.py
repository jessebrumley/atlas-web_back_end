#!/usr/bin/env python3
""" Module containing methods for authentication using Basic Auth.
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.base import Base
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class
        Implements methods to authenticate users based on credentials.
    """

    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """ Extracts the Base64 part of an authorization header.
            Returns None if the header is invalid or not of type str.
        """
        if auth_header is None or type(auth_header) is not str:
            return None
        if auth_header.split(" ")[0] != 'Basic':
            return None
        return auth_header.split(" ")[1]

    def decode_base64_authorization_header(self, auth_header_64: str) -> str:
        """ Decodes a Base64 encoded authorization header.
            Returns None if decoding fails.
        """
        if auth_header_64 is None or type(auth_header_64) is not str:
            return None
        try:
            result = base64.b64decode(auth_header_64).decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            result = None
        return result

    def extract_user_credentials(self, decoded_header: str) -> (str, str):
        """ Extracts user credentials (email and password) from the
            decoded authorization header.
            Returns (None, None) if extraction fails.
        """
        if (decoded_header is None or
                type(decoded_header) is not str or
                ':' not in decoded_header):
            return (None, None)
        extracted = decoded_header.split(':')
        return (extracted[0], extracted[1])

    def user_object_from_credentials(self, e: str, pw: str) -> TypeVar('User'):
        """ Retrieves a user object using provided email and password.
            Returns None if the user is not found or the password is invalid.
        """
        if e is None or type(e) is not str:
            return None
        if pw is None or type(pw) is not str:
            return None
        try:
            user_list = User.search({'email': e})
            if len(user_list) == 0:
                return None
            if not user_list[0].is_valid_password(pw):
                return None
            return user_list[0]
        except KeyError:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the User instance based on the current request.
            Extracts, decodes, and validates the authorization header
            to return the appropriate User object.
        """
        header = self.authorization_header(request)
        b64header = self.extract_base64_authorization_header(header)
        decoded_header = self.decode_base64_authorization_header(b64header)
        info = self.extract_user_credentials(decoded_header)
        user_object = self.user_object_from_credentials(info[0], info[1])
        return user_object
