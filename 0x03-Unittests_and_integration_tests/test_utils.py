#!/usr/bin/env python3
"""a TestAccessNestedMap class"""

import unittest
import pytest
from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """inherits from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, "a", KeyError(a)),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
                              self,
                              nested_map: Mapping,
                              path: Sequence,
                              res: Any) -> Any:
        """test function takes nested_map&path as arguments"""
        result = nested_map[key]
        self.assertEqual(result, res)
