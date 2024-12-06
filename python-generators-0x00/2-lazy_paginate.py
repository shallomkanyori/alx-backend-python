"""This module defines a generator that lazy loads paginated  user data from the database"""
from paginate_users import paginate_users

def lazy_paginate(page_size):
    """Lazy loads paginated user data"""

    offset = 0
    while True:
        rows = paginate_users(page_size, offset)
        if not rows:
            break
        offset += page_size
        yield rows
    return