#!/usr/bin/env python3
"""Function that takes in a list of floats and returns float sum"""


def sum_list(figs: list[float]) -> float:
    """function takes in two floats"""

    sum_float = 0.0
    for fig in figs:
        sum_float += fig

    return sum_float
