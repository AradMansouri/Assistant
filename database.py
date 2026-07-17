import sys
import sqlite3

connection = sqlite3.connect('assistant.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, note TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, due_time TEXT)''')

connection.commit()