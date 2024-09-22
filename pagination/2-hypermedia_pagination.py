#!/usr/bin/env python3
"""
Pagination module for baby names dataset.
"""

import csv
import math
from typing import List, Dict, Any


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
            A list of rows for the specified page, or an empty list if
            out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        if start_index >= len(data):
            return []

        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Compile the information for a page into a dictionary.

        Args:
            page: Current page number (default is 1).
            page_size: Number of items per page (default is 10).

        Returns:
            A dictionary with pagination information.
        """
        result = {}
        total_records = len(self.dataset())
        total_pages = math.ceil(total_records / page_size)

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        result['page_size'] = min(page_size,
                                  total_records - (page - 1) * page_size)
        result['page'] = page
        result['data'] = self.get_page(page, page_size)

        result['next_page'] = page + 1 if page < total_pages else None
        result['prev_page'] = page - 1 if page > 1 else None
        result['total_pages'] = total_pages

        return result
