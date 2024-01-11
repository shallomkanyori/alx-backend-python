#!/usr/bin/python3
"""Duck type and iterable object

Functions:
    element_length(lst)
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
