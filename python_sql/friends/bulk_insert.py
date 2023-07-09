import sqlite3

conn = sqlite3.connect("my_friends.db")

# create cursor object
c = conn.cursor(
)
people = [
    ("James", "Amundsen", 5),
    ("Mike", "Parks", 8),
    ("John", "Hudson", 7),
    ("Mike", "Armstrong", 7),
    ("Leo", "Boone", 3)]
# c.executemany("INSERT INTO friends VALUES (?,?,?);", people)
# c.execute(query, data)

for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?);", person)

# commit changes
conn.commit()
conn.close()
