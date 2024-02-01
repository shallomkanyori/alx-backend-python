#!/usr/bin/env python3
"""Tests the utils.access_nested_map method

Classes:
    TestAccessNestedMap
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map method"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any):
        """Tests the access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, expected: str):
        """Tests exceptions from the access_nested_map method"""
        with self.assertRaises(KeyError, msg=expected):
            access_nested_map(nested_map, path)
