import sqlite3
import random

# create a table called newnum if it doesn't exist	
connection = sqlite3.connect("newnum.db")

c = connection.cursor()
c.execute("DROP TABLE if exists numbers")
c.execute("CREATE TABLE numbers(num INT)")

for i in range(100):
	c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0, 100),))



connection.commit()
c.close()