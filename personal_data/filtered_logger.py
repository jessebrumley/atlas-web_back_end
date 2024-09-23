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


# Implement the main function
def main() -> None:
    """ Main function to retrieve and display user data from the database.
    """
    # Obtain a database connection
    db_connection = get_db()

    # Create a cursor to interact with the database
    cursor = db_connection.cursor()

    # Execute a query to retrieve all rows from the users table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Get the logger instance
    logger = get_logger()

    # Iterate through each row and log the data
    for row in rows:
        # Create a formatted log message with the row data
        log_message = f"name={row[0]}; email={row[1]}; phone={row[2]}; " \
                      f"ssn={row[3]}; password={row[4]}; ip={row[5]}; " \
                      f"last_login={row[6]}; user_agent={row[7]}"
        logger.info(log_message)

    # Close the cursor and connection
    cursor.close()
    db_connection.close()


# Ensure only the main function runs when the module is executed
if __name__ == "__main__":
    main()
