"""This file takes the csv data and converts it into a database/.db file"""
import sys
import os

sys.path.append("preprocess_SQL_files/")

from transform_data import transform

def test_transform():
    db = "nypd_shooting.db"
    transform_result = transform("data/nypd_shooting.csv")
    assert transform_result is not None

if __name__ == "__main__":
    test_transform()
