import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	for row in c.execute("SELECT firstname, lastname FROM employees"):
		print(row[0], row[1])
