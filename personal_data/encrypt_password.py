#!/usr/bin/env python3
"""
hash_password module will use bcrypt hashing to encrypt passwords.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashes a password using bcrypt.

    Arguments:
    password: The plain text password to be hashed.

    Returns:
    A salted, hashed password as a byte string.
    """
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
