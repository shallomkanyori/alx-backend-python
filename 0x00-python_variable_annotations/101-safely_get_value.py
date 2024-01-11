#!/usr/bin/python3
"""More involved type annotations

Functions:
    safely_get_value(dct, key, default)
"""
from typing import Mapping, TypeVar, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """Returns the value of a given key or a default if it does not exist."""

    if key in dct:
        return dct[key]
    else:
        return default
