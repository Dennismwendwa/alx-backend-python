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
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """Testing the access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple[str],
                                         expected: Exception,
                                         ) -> None:
        """Testing the access nested map method with wrong keys"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """Testing the get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Testing get_json method with valid data"""
        dic = {"json.return_value": test_payload}
        with patch("requests.get", return_value=Mock(**dic)) as re:
            self.assertEqual(get_json(test_url), test_payload)
            re.assert_called_once_with(test_url)


class TestMemoize(TestCase):
    """Testing memoize method"""

    def test_memoize(self) -> None:
        """This is the memoize class"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=lambda: 42,
                          ) as remember:
            test_c = TestClass()
            self.assertEqual(test_c.a_property(), 42)
            self.assertEqual(test_c.a_property(), 42)
            remember.assert_called_once()
