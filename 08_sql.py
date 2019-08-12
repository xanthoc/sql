import sqlite3

invs = [
	('Ford', 'Torus', 5),
	('Ford', 'Tico', 4),
	('Ford', 'Explorer', 3),
	('Honda', 'Accord', 2),
	('Honda', 'Icon', 1)
	]

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS inventory \
		(make TEXT, model TEXT, quantity INT)")
	c.executemany("INSERT INTO inventory \
		VALUES(?, ?, ?)", invs)
	for rows in c.execute("SELECT make, model, quantity \
		FROM inventory"):
		for item in rows:
			print(item, end=" ")
		print()

	c.execute("UPDATE inventory SET quantity=11 \
		WHERE model='Explorer'")

	for rows in c.execute("SELECT make, model, quantity \
		FROM inventory WHERE make='Ford'"):
		for item in rows:
			print(item, end=" ")
		print()
