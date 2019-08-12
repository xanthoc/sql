import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	c.execute("SELECT DISTINCT * FROM inventory")
	data = c.fetchall()
	for ea in data:
		print(ea[0], ea[1])
		print(ea[2])
		sql = "SELECT order_date FROM orders WHERE make='{}' AND model='{}'".format(ea[0], ea[1])
		#print(sql)
		for row in c.execute(sql):
			print(row[0])
		print()
