#!/usr/bin/env python3
"""
This function creates a tuple with a string and the square of a number.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with a string and the square of a number.

    Args:
        k (str): A string value.
        v (Union[int, float]): An integer or float value.

    Returns:
        Tuple[str, float]: A tuple where the 1st element is the string k
                           and the 2nd element is the square of v as a float.
    """
    return (k, float(v ** 2))
