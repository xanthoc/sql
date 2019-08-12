import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	c.execute("UPDATE population SET population=9000000 WHERE city='New York City'")
	c.execute("DELETE FROM population WHERE city='Boston'")
	for row in c.execute("SELECT city, state, population FROM population"):
		for item in row:
			print(item, end=" ")
		print()
