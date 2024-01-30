import sqlite3

DB_NAME = "temperatureApp.db"
TABLE_NAME = "temperature"

# Create Database and Table
def setup():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( tempID PRIMARY KEY AUTO_INCREMENT, value INT, time NUMERIC )')
    con.commit()


if __name__ == '__main__':
    setup()


