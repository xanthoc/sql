import sqlite3

sql = {
	"average": "SELECT avg(population) FROM population",
	"max": "SELECT max(population) FROM population",
	"min": "SELECT min(population) FROM population",
	"sum": "SELECT sum(population) FROM population",
	"count": "SELECT count(city) FROM population"
}

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	for key, value in sql.items():
		c.execute(value)
		result = c.fetchall()
		#print(result)
		print(key+":", result[0][0])
