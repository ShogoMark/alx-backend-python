#!/usr/bin/env python3
"""a TestAccessNestedMap class"""

import unittest
import pytest
from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence
from utils import access_nested_map
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
                                        _ex: Type[Exception])
    """function that checks exceptions"""
    try:
        access_nested_map(nested_map, path_elements)
    except KeyError as e:
        self.assertEqual(str(e), str(_ex))
        else:
            self.fail("Expected KeyError not raised.")
