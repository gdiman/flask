# insert command with error handler

import sqlite3

conn = sqlite3.connect("new.db") 
c = conn.cursor()

try: 
	c.execute("""CREATE TABLE employees (Empno INT, Empname TEXT, DeptNo INT, DeptName TEXT)""")
except:
	print("Table exists")


employees = [
(111, 'Michael', 10, 'Development'),
(112, 'Fletcher', 20, 'Sales'),
(113, 'Jeremy', 10, 'Development'),
(114, 'Carol', 20, 'Sales'),
(115, 'Evan', 20, 'Sales')
]

c.executemany("""INSERT INTO employees VALUES(?, ?, ?, ?)""", employees)

conn.commit()

conn.close()

	
	