import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

cur.execute("INSERT INTO test (student, specialty) VALUES (?, ?)",
            ('First student', 'nechto')
            )
cur.execute("INSERT INTO test (student, specialty) VALUES (?, ?)",
            ('Second student', 'nechto_two')
           )

    

connection.commit()
connection.close()
