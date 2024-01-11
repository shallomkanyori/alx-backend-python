#!/usr/bin/python3
"""Complex types - mixed list

Functions:
    sum_mixed_list(mxd_lst)
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of integers and floats"""
    return sum(mxd_lst)
