import sqlite3

conn = sqlite3.connect("new.db")

c = conn.cursor()

try:
	c.execute("INSERT INTO populations \
		VALUES('New York', 'NY', 8400000)")
	c.execute("INSERT INTO populations \
		VALUES('San Francisco', 'CA', 800000)")
	conn.commit()
except sqlite3.OperationalError:
	print("Oops! Something went wrong ...")
conn.close()