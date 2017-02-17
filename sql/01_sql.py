# SQL test file #

# import sqlite3 library
import sqlite3

#create a database if doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor to execute SQL commands
cursor = conn.cursor()

# execute many 
cities = [
    ('Boston', 'MA', 600000),
    ('Chicago', 'IL', 27000000),
    ('Houston', 'TX', 2100000),
    ('Phoenix', 'AZ', 15000000)
    ]

# create table 
# cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)""")
cursor.execute("INSERT INTO population VALUES('San Franciso', \
	'CA', 8300000)")
cursor.execute("INSERT INTO population VALUES('New York', \
	'NY', 10700000)")

cursor.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
conn.commit()

# close connection
cursor = conn.close()

