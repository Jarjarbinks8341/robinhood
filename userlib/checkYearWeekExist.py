import sqlite3

conn = sqlite3.connect("RobinhoodTrader.db")
cursor = conn.cursor()

"""
table_name = "trade_record"
key = "year_week_no"
value = "value"
"""

#cursor.execute("""
#CREATE TABLE IF NOT EXISTS trade_record (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    key TEXT,
#    value TEXT
#)
#""")
user_data = [('2024_W01', '{"key":"value"}')]
cursor.executemany("INSERT INTO trade_record (key, value) VALUES (?, ?)", user_data)

conn.commit()

cursor.execute("SELECT * FROM trade_record")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
