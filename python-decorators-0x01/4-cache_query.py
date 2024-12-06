"""This module defines a decorator that caches the result of a query"""
import functools
import sqlite3
import time

query_cache = {}

def cache_query(func):
    """Caches the result of a query"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function for caching query results"""
        
        key = kwargs.get('query')
        if key not in query_cache:
            query_cache[key] = func(*args, **kwargs)
        return query_cache[key]
    return wrapper

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
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

print("Before first call", query_cache)

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

print("After first call", query_cache)
#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")

print("After second call", query_cache)