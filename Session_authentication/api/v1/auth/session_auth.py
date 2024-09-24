#!/usr/bin/env python3
""" Session Authentication class module
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session Authentication class
        Implements session-based authentication
    """

    # Class attribute to store session ID -> user_id mappings
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id and stores it in the dictionary.

        Args:
            user_id (str): The ID of user for whom session is created.

        Returns:
            str: The generated Session ID, or None if the user_id is invalid.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a new Session ID using uuid4
        session_id = str(uuid.uuid4())

        # Store the session_id -> user_id in the dictionary
        self.user_id_by_session_id[session_id] = user_id

        # Return the generated session ID
        return session_id
