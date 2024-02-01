#!/usr/bin/env python3
"""Tests the utils module

Classes:
    TestAccessNestedMap
    TestGetJson
"""
import unittest
import requests
from unittest import mock
from parameterized import parameterized
from utils import (
        access_nested_map,
        get_json
)
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


class TestGetJson(unittest.TestCase):
    """Tests the get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Mapping):
        """Tests the get_json method"""

        with mock.patch('requests.get') as mock_get:
            mock_resp = mock.Mock(**{
                'json.return_value': test_payload
            })
            mock_get.return_value = mock_resp

            output = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            assert output == test_payload
