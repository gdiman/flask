import sqlite3
import random
import sqlite3

conn = sqlite3.connect("newnum.db")

c = conn.cursor()

brk = 4
while True:

	print("\n\n")
	print("Select a SQL operation on 100 random numbers (enter 5 to quit:\n")
	print("  1. AVG()")
	print("  2. MAX()")
	print("  3. MIN()")
	print("  4. SUM()\n")

	resp = input("Choice: ")
	if resp in set(["1", "2", "3", "4"]):
		operation = {1:"avg", 2:"max", 3:"min", 4:"sum"}[int(resp)]
		c.execute("SELECT {}(num) from numbers".format(operation))
		get = c.fetchone()
		print(operation + ":  %f" % get[0])
	else:
		
		print("Bye!\n")
		break
    	    
