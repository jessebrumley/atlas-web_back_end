#!/usr/bin/env python3
"""
This module defines variables and returns them.
"""


def func() -> return: tuple[int, float, bool, str]:
    """
    Returns static variables.

    Args:

    Returns:
        tuple: A tuple containing an integer, a float, a boolean, and a string.
    """

    a: int = 1
    pi: float = 3.14
    i_understand_annotations: bool = True
    school: str = "Holberton"

    return a, pi, i_understand_annotations, school
