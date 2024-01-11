#!/usr/bin/env python3
"""Duck type and iterable object

Functions:
    element_length(lst)
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples of the element in the sequence and its length.
    """
    return [(i, len(i)) for i in lst]
