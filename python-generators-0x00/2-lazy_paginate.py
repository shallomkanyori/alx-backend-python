"""This module defines a generator that lazy loads paginated  user data from the database"""
import seed

def paginate_users(page_size, offset):
    """Paginates the user data"""

    connection = seed.connect_to_prodev()
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()

    connection.close()

    return rows

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