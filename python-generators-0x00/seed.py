"""This module sets up a MySQL database."""
import MySQLdb
from MySQLdb import MySQLError
import csv

def connect_db() :
    """Connects to the MySQL database server"""

    try:
        connection = MySQLdb.connect()
        return connection
    except (MySQLError) as e:
        print(f"Error connecting to MySQL Platform: {e}")

def create_database(connection):
    """Creates the database ALX_prodev if it does not exist"""

    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
    except (MySQLError) as e:
        print(f"Error creating database: {e}")

def connect_to_prodev():
    """Connects the the ALX_prodev database in MySQL"""

    try:
        connection = MySQLdb.connect(db='ALX_prodev')
        return connection
    except (MySQLError) as e:
        print(f"Error connecting to ALX_prodev database: {e}")

def create_table(connection):
    """Creates a table user_data if it does not exists with the required fields"""

    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS user_data (id VARCHAR(60) PRIMARY KEY, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, age DECIMAL NOT NULL)")
        cursor.close()
    except (MySQLError) as e:
        print(f"Error creating table: {e}")

def insert_data(connection, data):
    """Inserts data in the database if it does not exist"""

    try:
        cursor = connection.cursor()

        with open(data, 'r') as file:
            user_data = csv.DictReader(file)

            query_data = [(row['id'], row['name'], row['email'], float(row['age'])) for row in user_data]

            cursor.executemany("INSERT INTO user_data (id, name, email, age) VALUES (%s, %s, %s, %s)", query_data)
        
        connection.commit()

        cursor.close()
    except (MySQLError) as e:
        print(f"Error inserting data: {e}")