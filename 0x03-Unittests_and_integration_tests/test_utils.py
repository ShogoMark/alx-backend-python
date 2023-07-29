#!/usr/bin/env python3
"""a TestAccessNestedMap class"""

import unittest
import pytest
from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """inherits from unittest.TestCase"""
    @parameterized.expand([
        (nested_map={"a": 1}, path=("a"), res=1),
        (nested_map={"a": {"b": 2}}, path=("a"), res=KeyError(a)),
        (nested_map={"a": {"b": 2}}, path=("a", "b"), res=2),
    ])
    def test_access_nested_map(
                              self,
                              nested_map: Mapping,
                              path: Sequence,
                              res: Any) -> Any:
        """test function takes nested_map&path as arguments"""
        result = nested_map[key]
        self.assertEqual(result, res)
