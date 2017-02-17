import sqlite3
import random
import sqlite3

conn = sqlite3.connect("newnum.db")

c = conn.cursor()

brk = 4
while brk <> 5:
	print("\n\n")
	print("Select a SQL operation on 100 random numbers (enter 6 to quit:\n")
	print("  1. AVG()\n")
	print("  2. COUNT()\n")
	print("  3. MAX()\n")
	print("  4. MIN()\n")
	print("  5. SUM()\n\n")

	resp = input("")
