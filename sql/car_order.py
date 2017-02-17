import sqlite3
import datetime

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	autos = c.execute("SELECT * FROM inventory")
	# ordered = c.execute("SELECT * FROM orders")
	rows = autos.fetchall()
	#orows = ordered.fetchall()

	# add 5 orders to orders for each car in inventory each with a diff date

#	i = datetime.datetime.now()
#	cnt = i.month + 1
#	for r in rows:
#		for n in range(0,4):
#			new_date = str(i.month)+'/'+str(cnt)+'/'+str(i.year)
#			autos.execute("INSERT INTO orders VALUES(?, ?, ?)", (r[0], r[1], new_date))
#			cnt = cnt + 1

# print inventory/quantities and orders
for r in rows:
	print("Make/Model: " + r[0]+"  "+ r[1])
	print("Qty: "+ str(r[2]))
	olist = c.execute("SELECT * FROM orders WHERE model = ?", (r[1],))
	tlist = olist.fetchall()
	for o in tlist:
		print("Ordered: " + o[2])

	mytot = c.execute("SELECT count(model) FROM orders WHERE model = ?", (r[1],))
	result = mytot.fetchone()
	print("Total "+ r[1] + "'s ordered: "+ str(result[0]) + '\n')
		


	

connection.commit()
connection.close()


