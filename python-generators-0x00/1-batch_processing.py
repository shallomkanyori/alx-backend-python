"""This modules creates a generator to fetch and process data in batches from the users database"""
import seed

def stream_users_in_batches(batch_size):
    """Fetches rows in batches"""

    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    for i in range(0, len(rows), batch_size):
        yield rows[i:i + batch_size]

def batch_processing(batch_size):
    """Processes each batch to filter users over the age of 25"""

    for batch in stream_users_in_batches(batch_size):
        for row in batch:
            if row[3] > 25:
                print(row)
    
    return