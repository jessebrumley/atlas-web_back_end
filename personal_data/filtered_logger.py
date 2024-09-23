#!/usr/bin/env python3
"""
filtered_logger module for obfuscating log messages.
"""

import re
from typing import List
import logging
import os
import mysql.connector
from mysql.connector import connection
import bcrypt


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """
    Returns the log message obfuscated by redacting sensitive fields.

    Arguments:
    fields: A list of strings representing all fields to obfuscate.
    redaction: A string representing what will replace the obfuscated fields.
    message: The log line to be obfuscated.
    separator: A string representing the separator character in the log line.

    Returns:
    The log message with specified fields redacted.
    """

    pattern = rf'({"|".join(fields)})=([^ {re.escape(separator)}]*)'

    return re.sub(pattern,
                  lambda match: f"{match.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initializes the formatter with specified fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.FIELDS = fields

    # Format the log record, filtering specified fields
    def format(self, record: logging.LogRecord) -> str:
        """ Formats the log record, filtering specified fields.
        """
        record.msg = filter_datum(self.FIELDS, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        return super().format(record)


# Create a constant tuple for PII fields
PII_FIELDS = (
    'name',
    'email',
    'phone',
    'ssn',
    'password'
)


# Create a logger object for user_data
def get_logger() -> logging.Logger:
    """ Creates and returns a logger object for user data.
    """
    # Initialize logger
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)

    # Attach handler to logger
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)

    # Prevent propagation to other loggers
    logger.propagate = False

    return logger


# Create a function to connect to the database
def get_db() -> connection.MySQLConnection:
    """ Connects to the MySQL database and returns the connection object.
    """
    # Retrieve credentials from environment variables
    usr = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    pw = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    hst = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    # Create a connection to the database
    cnx = mysql.connector.connect(
        user=usr,
        password=pw,
        host=hst,
        database=db_name
    )
    return cnx


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
