"""This module defines a decorator that automatically handles opening and closing database connections"""
import functools
import sqlite3

def with_db_connection(func):
    """Automatically handles opening and closing database connections"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function for opening and closing database connections"""
        
        conn = sqlite3.connect('users.db')
        result = func(conn, *args, **kwargs)
        conn.close()
        return result
    return wrapper

@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone()

#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)