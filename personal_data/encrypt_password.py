#!/usr/bin/env python3
"""
hash_password module will use bcrypt hashing to encrypt passwords.
is_valid uses bcrypt to check is hashed password and input password match.
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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates a password against a hashed password.

    Arguments:
    hashed_password: The hashed password as a byte string.
    password: The plain text password to validate.

    Returns:
    True if the password matches the hashed password, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
