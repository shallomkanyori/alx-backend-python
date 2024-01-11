#!/usr/bin/env python3
"""Complex types - functions

Functions:
    make_multiplier(multiplier)
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""

    def mult_fun(x: float) -> float:
        return x * multiplier

    return mult_fun
