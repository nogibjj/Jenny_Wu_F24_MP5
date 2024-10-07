import sqlite3
import os


def query_create(database, table, colnames, values):
    """Creates an entry into the specified table"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table} ({colnames}) VALUES ({values})")
    return "Success"


def query_read(database, table):
    """Query the database to read the top 5 rows of the specified table"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table} LIMIT 5")
    print(f"Top 5 rows of the {table} table:")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    return "Success"


def query_update(database, table, column, new_value, Incident_Key):
    """Update a specific column in a row based on incident key"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    query = f"UPDATE {table} SET {column} = ? WHERE Incident_Key= ?"
    cursor.execute(query, (new_value, Incident_Key))
    affected_rows = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()

    if affected_rows == 0:
        print("No record found")
    print("Record updated successfully!")


def query_delete(database, table, Incident_Key):
    """Deletes a specific column in a row based on incident key"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    query = f"DELETE FROM {table} WHERE Incident_Key= ?"
    cursor.execute(query(Incident_Key))
    changed_rows = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()

    if changed_rows == 0:
        print("No record found")
    print("Record deleted successfully!")
