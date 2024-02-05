#!/usr/bin/env python3
"""This script test the utils module"""
from typing import Union, Dict, Tuple
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, patch
from unittest import TestCase

from utils import get_json, access_nested_map, memoize


class TestAccessNestedMap(TestCase):
    """Testing the utils module"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map_method(self, nested_map: Dict,
                                      path: Tuple[str],
                                      expected: Union[Dict, int]) -> None:
        """Testing the access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_mwthod_with_wrong_keys(self, nested_map: Dict,
                                                      path: Tuple[str],
                                                      expected: Exception,
                                                      ) -> None:
        """Testing the access nested map method with wrong keys"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)
