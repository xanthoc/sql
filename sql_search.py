import sqlite3

sqls = {
	"AVG": "SELECT avg(num) FROM nums",
	"MAX": "SELECT max(num) FROM nums",
	"MIN": "SELECT min(num) FROM nums",
	"SUM": "SELECT sum(num) FROM nums"
}

with sqlite3.connect("newnum.db") as conn:
	c = conn.cursor()
	while True:
		ans = input("What do you want? [AVG, MAX, MIN, SUM, QUIT] ")
		if ans.upper() == 'QUIT':
			print("Bye ... ")
			break
		#print(ans.upper())
		if ans.upper() in sqls.keys():
			c.execute(sqls[ans.upper()])
			print(c.fetchall()[0][0])
		else:
			print("Your choice is not supported. Please try again ...")
