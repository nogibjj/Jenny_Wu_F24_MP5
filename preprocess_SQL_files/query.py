import sqlite3
import os

from preprocess_SQL_files.extract_data import extract
from preprocess_SQL_files.transform_data import load

extract()
load()


def query(database="nypd_shooting.db"):
    """Query the database for the top 5 rows of the specified table"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {database} LIMIT 5")
    print(f"Top 5 rows of the {database} table:")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    return "Success"


query()
