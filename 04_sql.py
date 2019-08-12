import csv
import sqlite3

employees = csv.reader(open("employees.csv", "r"))
with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS \
		employees(firstname TEXT, lastname TEXT)")
	c.executemany("INSERT INTO employees \
		VALUES(?, ?)", employees)