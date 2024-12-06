"""This module defines a generator to compute a memory-efficient aggregate function."""
import seed

def stream_user_ages():
    """Streams user ages from the database"""

    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data;")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    for row in rows:
        yield row[0]

def get_average_age():
    """Computes the average age of users"""

    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    
    average = round(total / count, 2)
    print(f"Average age of users: {average}")

    return average