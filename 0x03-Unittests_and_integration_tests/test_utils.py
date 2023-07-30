#!/usr/bin/env python3
"""a TestAccessNestedMap class"""

import unittest
from unittest.mock import patch, Mock
import pytest
from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence, Type
from utils import access_nested_map, get_json
import requests


class TestAccessNestedMap(unittest.TestCase):
    """inherits from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, "a", KeyError("a")),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            res: Any) -> Any:
        self.assertEqual(access_nested_map(nested_map, path), res)

    @parameterized.expand([
        ({}, "a", KeyError),
        ({"a": 1}, "a", "b", KeyError),
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping,
            *path_elements: Sequence,
            expected_exception: Type[Exception]):
        """function that checks exceptions"""
        try:
            access_nested_map(nested_map, path_elements)
        except KeyError as e:
            self.assertEqual(str(e), str(expected_exception))
        else:
            self.fail("Expected KeyError not raised.")


class TestGetJson(unittest.TestCase):
    """Class inherits from Testcase"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, Any]) -> None:
        """function takes in test_url and test_payload as args"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('utils.get_json') as mock_get_json:
            mock_get_json.return_value = mock_response

            result = get_json(test_url)

            self.assertEqual(result, test_payload)
            mock_get_json.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
