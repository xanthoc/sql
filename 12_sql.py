import sqlite3
import random

orders = []
for _ in range(10):
	date = '1998-'
	date += str(random.choice([1, 3, 5])) + '-'
	date += str(random.choice([15, 25, 28]))
	orders.append(('Ford', random.choice(['Explorer', 'Torus', 'Tico']), date))
for _ in range(5):
	date = '1998-'
	date += str(random.choice([1, 3, 5])) + '-'
	date += str(random.choice([15, 25, 28]))
	orders.append(('Honda', random.choice(['Civic', 'Accord', 'Icon']), date))


for o in orders:
	print(o)

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS orders (make TEXT, model TEXT, order_date TEXT)")
	c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)
