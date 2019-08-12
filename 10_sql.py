import sqlite3

cities = [
	('New York City', 'Northeast'),
	('San Francisco', 'West'),
	('Chicago', 'Midwest'),
	('Houston', 'South'),
	('Phoenix', 'West'),
	('Boston', 'Northeast'),
	('Los Angeles', 'West'),
	('Houston', 'South'),
	('Philadelphia', 'Northeast'),
	('San Antonio', 'South'),
	('San Diego', 'West'),
	('Dallas', 'South'),
	('San Jose', 'West'),
	('Jacksonville', 'South'),
	('Indianapolis', 'Midwest'),
	('Austin', 'South'),
	('Detroit', 'Midwest')
	]

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS regions (city TEXT, region TEXT)")
	c.executemany("INSERT INTO regions VALUES(?, ?)", cities)
	for row in c.execute("SELECT * FROM regions ORDER BY region ASC"):
		for item in row:
			print(item, end=", ")
		print()
