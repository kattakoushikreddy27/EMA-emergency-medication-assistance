import sqlite3

conn = sqlite3.connect('medications.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE medications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        formula TEXT NOT NULL,
        uses TEXT NOT NULL,
        dosage TEXT NOT NULL,
        warnings TEXT NOT NULL,
        effects TEXT NOT NULL,
        alternatives TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
