#!/usr/bin/env python3
"""
This function creates a tuple with a string and the square of a number.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value to use in the multiplication.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
                                   the result of multiplying it.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
