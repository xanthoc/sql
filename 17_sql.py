import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	c.execute("SELECT DISTINCT model FROM orders")
	models = c.fetchall()
	#print(models)
	for ea in models:
		sql = "SELECT count(order_date) FROM orders WHERE model='{}'".format(ea[0])
		#print(sql)
		c.execute(sql)
		cnt = c.fetchall()
		print("The total orders for {}:".format(ea[0]), cnt[0][0])
