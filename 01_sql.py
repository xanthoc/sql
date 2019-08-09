import sqlite3
conn = sqlite3.connect("new.db")
c = conn.cursor()
c.execute("CREATE TABLE population (city TEXT, state TEXT, population INT)")
conn.close()