#!/usr/bin/env python3
"""
Pagination module for baby names dataset.
"""

import csv
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Retrieve and cache the dataset from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                self.__dataset = [row for row in reader][1:]  # Skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of data.

        Args:
            page: Current page number (default is 1).
            page_size: Number of items per page (default is 10).

        Returns:
            A list of rows for specified page, or empty list if out of range
        """
        # Validate input parameters
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        if start_index >= len(data):
            return []

        return data[start_index:end_index]
