# This code is used to test if sqlite3 is working correctly in the environment.
# If this script runs without errors, it indicates that sqlite3 is properly installed and functional.
import sqlite3
print("sqlite3 is working!")

# Create a simple table
import sqlite3

conn = sqlite3.connect('satyalens.db')  # Creates file if not exists
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
''')

conn.commit()
conn.close()

cursor.execute('''
    INSERT OR IGNORE INTO users (user_id, platform, username)
    VALUES (?, ?, ?)
''', ('user123', 'telegram', 'alice'))
conn.commit()

cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
for user in users:
    print(user)

cursor.execute('''
    UPDATE users SET username = ? WHERE user_id = ?
''', ('newalice', 'user123'))
conn.commit()

cursor.execute('DELETE FROM users WHERE user_id = ?', ('user123',))
conn.commit()
conn.close()
