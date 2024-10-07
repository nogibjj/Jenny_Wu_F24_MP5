"""Asserting that the Data is being extracted from the url"""

import sys
import os

sys.path.append("preprocess_SQL_files/")
from extract_data import extract

def test_extract():
    url = "https://data.cityofnewyork.us/api/views/833y-fsy8/rows.csv?accessType=DOWNLOAD"
    test_path = "data/nypd_shooting.csv"
    folder = "data"
    result = extract()
    assert os.path.exists(result)
    


if __name__ == "__main__":
    test_extract()