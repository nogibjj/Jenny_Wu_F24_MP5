"""
Extract a dataset from a URL and place it into a database

NYPD Shooting dataset
"""

import requests

url="https://data.cityofnewyork.us/api/views/833y-fsy8/rows.csv?accessType=DOWNLOAD"
file_path="data/nypd_shooting.csv"
def extract(url, file_path):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
