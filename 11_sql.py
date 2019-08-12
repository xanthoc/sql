import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	for row in c.execute("SELECT DISTINCT population.city, population.population, regions.region \
		FROM population, regions WHERE population.city=regions.city \
		ORDER BY population.city ASC"):
		for item in row:
			print(item, end=", ")
		print()