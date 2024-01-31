import sqlite3
import datetime

DB_NAME = "temperatureApp.db"
TABLE_NAME = "temperature"

# Create Database and Table
def setup():
    execute_with_connection(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( id INTEGER PRIMARY KEY AUTOINCREMENT, degree REAL, humidity REAL, timestamp NUMERIC, location TEXT )'
    )


def execute_with_connection(query, attributes = None):
    try:
        con = sqlite3.connect(DB_NAME)
    except:
        print("Connection to DB couldn't be established.")
    cur = con.cursor()
    if attributes is None:
        cur.execute(query)
        for x in cur.fetchall():
            print(x)

    else:
        cur.execute(query, attributes)
    con.commit()
    con.close()

def insert_values(degree, humidity, location):
    time_raw = datetime.datetime.now()
    timestamp = time_raw.strftime("%Y%m%d%H%M%S")
    execute_with_connection(
        f'INSERT INTO {TABLE_NAME} (degree, humidity, location, timestamp) VALUES (?, ?, ?, ?)', (degree, humidity, location, timestamp)
    )

def get_max_temp(location):
    if location == None:
        execute_with_connection(
            f'SELECT MAX(degree) FROM {TABLE_NAME} GROUP BY degree'
        )
    else:
        execute_with_connection(
            f'SELECT MAX(degree) FROM {TABLE_NAME} WHERE location = ?', (location,)
        )

def get_min_temp(location):
    if location == None:
        execute_with_connection(
            f'SELECT MIN(degree) FROM {TABLE_NAME} GROUP BY degree'
        )
    else:
        execute_with_connection(
            f'SELECT MIN(degree) FROM {TABLE_NAME} WHERE location = ?', (location,)
        )

def get_latest_temp(location):
    if location == None:
        execute_with_connection(
            f'SELECT degree FROM {TABLE_NAME}'
        )
    else:
        execute_with_connection(
            f'SELECT degree FROM {TABLE_NAME} WHERE location = ? HAVING MAX(timestamp)', (location,)
        )

def get_latest_humidity(location):
    if location == None:
        execute_with_connection(
            f'SELECT .humidity FROM {TABLE_NAME}'
        )
    else:
        execute_with_connection(
            f'SELECT humidity FROM {TABLE_NAME} WHERE location = ? HAVING MAX(timestamp)', (location,)
        )

if __name__ == '__main__':
    setup()
    get_max_temp('abc')
    # execute_with_connection(f'SELECT * FROM {TABLE_NAME}')