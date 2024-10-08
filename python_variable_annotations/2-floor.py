#!/usr/bin/env python3
"""
This module takes in a float and returns the largest integer
less than or equal to the input
"""
import math


def floor(n: float) -> int:
    """
    Returns the largest integer less than or equal to input.

    Args:
      n(float): A float.

    Returns:
      int: largest integer less than or equal to input.
    """
    return math.floor(n)
