"""This file takes the csv data and converts it into a database/.db file"""

from preprocess_SQL_files.transform_data import transform

def test_transform():
    db = "remotehealthDB.db"
    transform_result = transform("data/remote_work_mental_health_data.csv")
    assert transform_result is not None


if __name__ == "__main__":
    test_transform()
