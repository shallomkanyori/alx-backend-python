#!/usr/bin/python3
"""Complex types - list of floats

Functions:
    sum_list(input_list)
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of elements in a list of floats."""
    return sum(input_list)
