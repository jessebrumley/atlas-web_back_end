#!/usr/bin/env python3
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscates specified fields in a log message."""
    pattern = f'({"|".join(map(re.escape, fields))})=.*?({separator}|$)'
    return re.sub(pattern, lambda m: f'{m.group(1)}={redaction}{m.group(2)}', message)
