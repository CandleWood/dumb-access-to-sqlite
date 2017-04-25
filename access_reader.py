"""
A completely stupid simple Access to SQLite conversion that will probably break with any complex databases (for now)
"""

import csv
import os
import sqlite3
import subprocess
import sys

access_db = sys.argv[1]
sqlite_db = os.path.splitext(os.path.basename(access_db))[0] + '.db'

if os.path.exists(sqlite_db):
    os.remove(sqlite_db)

# First get the table names
tables_exec = subprocess.check_output(['mdb-tables', access_db])
tables_list = tables_exec.decode('utf-8').strip().split(' ')

# Connect to the SQLite database
dbconnect = sqlite3.connect(sqlite_db)
c = dbconnect.cursor()

# Get the database schema
schema_exec = subprocess.check_output(['mdb-schema', access_db])
schema_query = schema_exec.decode('utf-8').strip().split("\n\n")

for q in schema_query:
    c.execute(q)

# Table imports
for table in tables_list:
    csv_export = subprocess.check_output(['mdb-export', '-H', access_db, table]).decode('utf-8')

    for entry in csv_export.split("\n"):
        if not entry:
            continue

        if ',,' in entry:
            entry = entry.replace(',,', ',NULL,')
        if entry[-1:] == ',':
            entry = '{0},NULL'.format(entry[:-1])

        c.execute('INSERT INTO {0} VALUES ({1})'.format(table, entry))

# Close the connection
dbconnect.commit()
dbconnect.close()
