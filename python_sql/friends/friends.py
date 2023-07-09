import sqlite3

conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO friends
#                     VALUES ('Merriwether', 'Lewis', 7)'''
# Bad do not do like this
# first_name = "Makhanya"
# last_name = "Mzili"
# age = 30
# query = f"INSERT INTO friends VALUES ('{first_name}','{last_name}',{age});"

# Better way!
# first_name = "Hlumela"
# last_name = "Mzili"
# age = 32
# query = f"INSERT INTO friends VALUES (?,?,?);"
# c.execute(query, (first_name, last_name, age))

data = ("Sino", "Sonamzi", 29)
query = "INSERT INTO friends VALUES (?,?,?);"
c.execute(query, data)
# commit changes
conn.commit()
conn.close()
