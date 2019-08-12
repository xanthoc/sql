import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	c.execute("SELECT i.make, i.model, quantity, order_date FROM inventory i INNER JOIN orders o ON i.model=o.model ORDER BY i.model ASC")
	data = c.fetchall()
	for ea in data:
		print(ea[0], ea[1])
		print(ea[2])
		print(ea[3])
		print()

