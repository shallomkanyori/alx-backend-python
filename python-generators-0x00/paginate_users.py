"""This module defines a function that paginates user data from the database"""
import seed

def paginate_users(page_size, offset):
    """Paginates the user data"""

    connection = seed.connect_to_prodev()
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()

    connection.close()

    return rows