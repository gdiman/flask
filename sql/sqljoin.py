import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	try:
		c.execute("""CREATE TABLE regions (city TEXT, region TEXT)""")
	except:
		print("Exists!")

	cities = [
	('San Franciso', 'Far West'),
	('New York City', 'Northeast'),
	('Chicago', 'Northcentral'),
	('Phoenix', 'Southwest'),
	('Boston', 'Central'),
	()
	]

	# c.executemany("INSERT INTO regions VALUES(?,?)", cities)

	#c.execute("SELECT * FROM regions ORDER BY region ASC")
	c.execute("""SELECT population.population, population.city, regions.region 
		FROM population, regions WHERE population.city = regions.city""")

	rows = c.fetchall()

	for r in rows:
		print(r[0], r[1])

connection.commit()
connection.close()


