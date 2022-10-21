import sqlite3
from estimate_constructor import config

connection = sqlite3.connect('../database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO unit (name) VALUES (?)",
            ('шт.',)
            )
cur.execute("INSERT INTO unit (name) VALUES (?)",
            ('м.п.',)
            )
cur.execute("INSERT INTO unit (name) VALUES (?)",
            ('м.кв.',)
            )

cur.execute("INSERT INTO items (code, name, price, unit_id) VALUES (?, ?, ?, ?)",
            ('AA3', 'Арматура А-3', '44,53', '1')
            )
cur.execute("INSERT INTO items (code, name, price, unit_id) VALUES (?, ?, ?, ?)",
            ('JB3', 'Железобетонные сваи', '2030', '2')
            )

cur.execute("INSERT INTO works (code, name, price, unit_id) VALUES (?, ?, ?, ?)",
            ('J01', 'Устройство ленточного фундамента', '330', '2')
            )
cur.execute("INSERT INTO works (code, name, price, unit_id) VALUES (?, ?, ?, ?)",
            ('J02', 'Устройство стяжки', '530', '2')
            )

connection.commit()
connection.close()
