#!/usr/bin/env python3
"""Unit tests for access_nested_map function."""

import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Tuple
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map."""

    @parameterized.expand([
        ("simple_key", {"a": 1}, ("a",), 1),
        ("nested_key", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("deeply_nested_key", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, name: str, nested_map: Mapping[str, Any], path: Sequence[str], expected: Any
    ) -> None:
        """Test access_nested_map returns expected output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main(verbosity=0)
