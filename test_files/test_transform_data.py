import sys
from transform_data import transform

sys.path.append("preprocess_SQL_files/")

"""This file takes the csv data and converts it into a database/.db file"""


def test_transform():
    transform_result = transform()
    assert transform_result is not None


if __name__ == "__main__":
    test_transform()
