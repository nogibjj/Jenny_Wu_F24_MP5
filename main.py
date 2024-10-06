from SQL_files.extract_data import extract
from SQL_files.transform_data import transform
from SQL_files.query_data import query_create, query_read, query_update, query_delete

extract()
transform()

query_create(database="nypd_shooting.db", table="nypd_shooting", colnames="", values="")

query_read(database="nypd_shooting.db", table="nypd_shooting")

query_update(database="nypd_shooting.db", table="nypd_shooting")

query_delete(database="nypd_shooting.db", table="nypd_shooting")
