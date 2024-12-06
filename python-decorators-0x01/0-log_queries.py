"""This module defines a decorator that logs database queries executed by any function"""
import functools
import sqlite3
from datetime import datetime

def log_queries(func):
    """Logs a database query executed by a function"""

    @functools.wraps(func)
    def wrapper(query):
        """Wrapper function for logging queries"""
        
        print(f"Query {query} executed at {datetime.now()}")
        return func(query)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")