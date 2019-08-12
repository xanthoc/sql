import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	c.execute("SELECT DISTINCT make, model, quantity FROM inventory")
	items = c.fetchall()
	for ea in items:
		print(ea[0], ea[1])
		print("quantity:", ea[2])
		c.execute("SELECT count(order_date) FROM orders WHERE model=?", (ea[1],))
		print("order:", c.fetchall()[0][0])