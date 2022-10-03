#!/usr/bin/env python3
"""Test cases for utils class
"""
import unittest
from unittest import mock
from parameterized import parameterized
from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Test access nested map function"""

    @parameterized.expand([

        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2 )

        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access nested map function"""

        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([

        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))

        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access nested map function"""

        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """Test get json function"""
    @parameterized.expand([

        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),

        ])
    def test_get_json(self, url, payload):
        """Test get json function"""
        with mock.patch("requests.get") as test_mock:
            test_mock.return_value.json.return_value = payload
            self.assertEqual(get_json(url), payload)

class TestMemoize(unittest.TestCase):
    """Test memoizefunction"""
    def test_memoize(self):
        """Test memoizefunction"""


        class TestClass:
            """class test class inside test memoize"""
            def a_method(self):
                """method inside class test_memoize"""

                return 42

            @memoize
            def a_property(self):
                """method inside class test_memoize"""

                return self.a_method()

        with mock.patch.object(TestClass, "a_method", return_value=42) as test_mock:
            my_object = TestClass()
            self.assertEqual(my_object.a_property, 42)
            self.assertEqual(my_object.a_property, 42)

            test_mock.assert_called_once()
