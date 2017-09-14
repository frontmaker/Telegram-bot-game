import sqlite3


def create_connection(database):
	try:
		conn = sqlite3.connect(database)
		return conn
	except Error as e:
		print(e)


def select_all(conn):
	cursor = conn.cursor()
	with conn:
		return cursor.execute("SELECT * FROM music").fetchall()

def select_single(conn, id):
	cursor = conn.cursor()
	with conn:
		return cursor.execute('SELECT * FROM music WHERE id = ?', (id, )).fetchall()[0]

def update_sigle(conn, key, id):
	cursor = conn.cursor()
	with conn:
		print(cursor.execute('UPDATE music SET chat_id = ? WHERE id = ?', (key, id, )).fetchall())
		# return cursor.execute('UPDATE music SET chat_id = ? WHERE id = ?', (key, id, )).fetchall()

def count_rows(conn):
	cursor = conn.cursor()
	with conn:
		return len(cursor.execute("SELECT * FROM music").fetchall())

def close(conn):
	conn.close()
