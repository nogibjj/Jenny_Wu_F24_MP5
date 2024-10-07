import sqlite3
import sys

sys.path.append("preprocess_SQL_files/")
from query_data import (
    query_create,
    query_read,
    query_update,
    query_delete,
    query_1,
    query_2,
)


def test_query_create():
    # Define the expected values to check
    expected_values = (
        228566043,
        "5/03/21",
        "3:53:00",
        "BRONX",
        41,
        0,
        "FALSE",
        "18-25",
        "M",
        "WHITE HISPANIC",
        "18-24",
        "M",
        "WHITE HISPANIC",
    )

    # Connect to the database
    conn = sqlite3.connect("nypd_shooting.db")
    cursor = conn.cursor()

    

    # Query to select the row that matches the expected values

    cursor.execute(
        """
        SELECT * FROM nypd_shooting 
        WHERE Incident_Key = ?
          AND Occur_Date = ?
          AND Occur_Time = ?
          AND Boro = ?
          AND Precinct = ?
          AND Jurisdiction_Code = ?
          AND Stat_Murder_Flag = ?
          AND Perp_Age_Group = ?
          AND Perp_Sex = ?
          AND Perp_Race = ?
          AND Vicitm_Age_Group = ?
          AND Victim_Sex = ?
          AND Victim_Race = ?
    """,
        expected_values,
    )

    # Fetch the result
    result = cursor.fetchone()

    # Assert that the result matches the expected values
    assert result == expected_values, f"Expected {expected_values} but got {result}"

    # Close the cursor and connection
    cursor.close()
    conn.close()

    print("Test passed: Entry exists in the database.")


# Run the test
test_query_create()


if __name__ == "__main__":
    test_query_create,
    test_query_read,
    test_query_update,
    test_query_delete,
    test_query_1,
    test_query_2
