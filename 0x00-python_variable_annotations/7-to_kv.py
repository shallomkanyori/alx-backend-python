#!/usr/bin/python3
"""Complex types - string and int/float to tuple

Functions:
    to_kv(k, v)
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns the tuple (k, v ** 2)"""
    return (k, v ** 2)
