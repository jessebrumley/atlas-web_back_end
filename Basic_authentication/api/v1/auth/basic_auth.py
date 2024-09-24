#!/usr/bin/env python3
"""Basic Authentication module.

This module defines the BasicAuth class, which inherits from the Auth class
to implement basic authentication for the API.
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth.

    This class implements basic authentication methods and functionalities
    to handle user authentication.
    """
    def handle_status_request(self, request):
        # Do nothing special for status request
        pass
