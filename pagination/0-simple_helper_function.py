#!/usr/bin/env python3
"""
This module provides a function to calculate pagination indices.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate the start and end indices for a specified page.

    Args:
        page: The page number (1-indexed).
        page_size: The number of items per page.

    Returns:
        A tuple containing the start index and the end index for the page.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
