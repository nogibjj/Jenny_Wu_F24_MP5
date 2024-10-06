"""Asserting that the Data is being extracted from the url"""

from preprocess_SQL_files.extract_data import extract
import os

def test_extract():
    url = "https://data.cityofnewyork.us/api/views/833y-fsy8/rows.csv?accessType=DOWNLOAD"
    test_path = "data/nypd_shooting.csv"
    folder = "data"
    result = extract()
    assert os.path.exists(result)
    
    os.remove(result)


if __name__ == "__main__":
    test_extract()