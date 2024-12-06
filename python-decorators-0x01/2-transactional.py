"""This module defines a decorator that manages database transactions"""
import functools
import sqlite3

def transactional(func):
    """Manages database transactions"""

    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        """Wrapper function for managing database transactions"""
            
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        return result
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
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

#### Update user's email with automatic transaction handling 
update_user_email(user_id=15, new_email='Crawford_Cartwright@hotmail.com')