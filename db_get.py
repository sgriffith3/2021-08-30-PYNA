import sqlite3

conn = sqlite3.connect("menu.db")

conn.execute("CREATE TABLE IF NOT EXISTS desserts (ID INT PRIMARY KEY, NAME TEXT, PRICE REAL);")
conn.commit()

#conn.execute("INSERT INTO desserts (NAME,PRICE) values ('creme brulee', 7.50)")
#conn.commit()
cursor = conn.execute("SELECT * FROM desserts")

for snack in cursor.fetchall():
    print(f"The {snack[1]} is ${snack[2]}")
