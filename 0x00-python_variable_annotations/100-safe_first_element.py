#!/usr/bin/env python3
"""Duck typing - first element of a sequence

Functions:
    safe_first_element(lst)
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence"""

    if lst:
        return lst[0]
    else:
        return None
