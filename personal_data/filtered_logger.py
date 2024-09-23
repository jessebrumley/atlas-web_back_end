#!/usr/bin/env python3
"""
filtered_logger module for obfuscating log messages.
"""

import re
from typing import List
import logging


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

    def format(self, record: logging.LogRecord) -> str:
        """ Formats the log record, filtering specified fields.
        """
        record.msg = filter_datum(self.FIELDS, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        return super().format(record)
