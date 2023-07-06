#!/usr/bin/env python3
"""Function that takes in a list of floats and returns float sum"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """function takes in list of floats"""

    sum_float = 0.0
    for lists in input_list:
        sum_float += lists

    return sum_float
