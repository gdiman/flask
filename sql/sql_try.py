# insert command with error handler

import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

try:

	cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 840000)")
	cursor.execute("INSERT INTO populations VALUES('San Franciso', ,CA, 800000)")

	conn.commit()	

except sqlite3.OperationalError:

	print('Oops! Something went wrong, Try again...')

conn.close()