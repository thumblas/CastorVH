#from os import getenv
import pymssql

# server = getenv("localhost")
# user = getenv("SA")
# password = getenv("sql@23456789")

conn = pymssql.connect("localhost", "SA", "sql@23456789", "TestDB")
cursor = conn.cursor()
# cursor.execute("""
# IF OBJECT_ID('persons', 'U') IS NOT NULL
#     DROP TABLE persons
# CREATE TABLE persons (
#     id INT NOT NULL,
#     name VARCHAR(100),
#     salesrep VARCHAR(100),
#     PRIMARY KEY(id)
# )
# """)
cursor.execute(
    "INSERT INTO DATA VALUES (%s, %s, %s, %d, %s)",
    ('tjirjitr', 'John Smith', 'John Doe', 232, 'fjgdjgdf'))
# you must call commit() to persist your data if you don't set autocommit to True
conn.commit()

cursor.execute('SELECT * FROM DATA WHERE State=%s', 'John Doe')
row = cursor.fetchone()
while row:
    print(" Name=%s" % (row[0]))
    row = cursor.fetchone()

conn.close()



#sqlcmd -S localhost -U SA -P 'sql@23456789'
