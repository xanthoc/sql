import random
import sqlite3

with sqlite3.connect("newnum.db") as conn:
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS nums")
	c.execute("CREATE TABLE IF NOT EXISTS nums (num INT)")
	for _ in range(100):
		c.execute("INSERT INTO nums VALUES(?)", (random.randint(0, 100),))
