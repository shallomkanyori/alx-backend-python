"""This module defines a decorator that retries database operations if they fail"""
import sqlite3
import functools
import time

def retry_on_failure(_func=None, *, retries=3, delay=2):
    """Retries a function that interacts with a database"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except sqlite3.OperationalError:
                    time.sleep(delay)
            return func(*args, **kwargs)
        return wrapper
    
    if _func is None:
        return decorator
    else:
        return decorator(_func)

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
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)