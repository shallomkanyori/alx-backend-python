#!/usr/bin/env python3
"""Type Checking

Functions:
    zoom_array(lst, factor)
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms into a tuple by increasing the count of each element to factor.

    Args:
        lst: The tuple
        factor: The factor by which to zoom in. Default is 2.

    Returns:
        A list of the zoomed in tuple.
    """

    zoomed_in: List = [
            item for item in lst
            for i in range(factor)
            ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
