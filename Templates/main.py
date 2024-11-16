import sqlite3


connection = sqlite3.connect("database.sqlite")
cursor= sqlite3.Cursor(connection)


request = ("CREATE TABLE IF NOT  EXISTS brawler"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "rares VARCHAR(255),"
           "description VARCHAR(255),"
           "hp INTEGER,"
           "yron INTEGER,"
           "hypercharge VARCHAR(255))")
cursor.execute(request)

insert_request = ("INSERT INTO brawler" "(name, rares, description, hp, yron, hypercharge) VALUES (?, ?, ?, ?, ?, ?)")

cursor.execute(insert_request, ("Шелли", "common", "Шелли — идеальный рейнджер. Она ответственная, выносливая и непревзойдённо обращается с ружьём, и ей непонятно, как Кольт перетянул всё внимание на себя", "7400", "3000", "yes"))

text = cursor.execute("SELECT * FROM brawler")
print(text.fetchall())