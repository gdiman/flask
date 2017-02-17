# insert command with error handler

import sqlite3

conn = sqlite3.connect("cars.db") 

c = conn.cursor()

rows = c.execute("SELECT * FROM inventory")


for r in rows:
	print(r[0], r[1], r[2])

change_val = 0
change_car = 'Accord'

while len(change_car) > 0:
	change_car = input("Change inventory on what car: ")
	change_val =  int(input("New inventory number: "))
	print(str(change_val))

	rows.execute("""UPDATE inventory SET Quantity = ? WHERE Model = ?""", (change_val, change_car))

conn.commit()
conn.close()

