"""This module defines a generator that streams rows from the user_data table one by one"""
import seed

def stream_users():
    """Streams rows from the user_data table in the ALX_prodev database"""

    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    for row in rows:
        yield row