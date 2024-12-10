"""This module defines a class based reusable query context manager"""
import sqlite3

class ExecuteQuery:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.query = 'SELECT * FROM users WHERE age > ?'
        self.parameter = 25

        self.results = self.conn.execute(self.query, (self.parameter,)).fetchall()
    
    def __enter__(self):
        return self.results
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
    

with ExecuteQuery('users.db') as results:
    print(results)