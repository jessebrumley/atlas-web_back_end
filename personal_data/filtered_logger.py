#!/usr/bin/env python3
"""
filtered_logger module for obfuscating log messages.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
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
    # Create a single regex pattern that matches any of the fields followed by "=value"
    pattern = f'({"|".join(map(re.escape, fields))})=.*?({separator}|$)'
    # Replace the matched fields with the redacted value
    return re.sub(pattern, lambda m: f'{m.group(1)}={redaction}{m.group(2)}', message)
