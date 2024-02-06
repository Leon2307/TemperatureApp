import sqlite3
import datetime

DB_NAME = "temperatureApp.db"
TABLE_NAME = "temperature"


# Function to set up the database table if it doesn't exist
def setup():
    execute_with_connection(
        f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( id INTEGER PRIMARY KEY AUTOINCREMENT, degree REAL, humidity REAL, timestamp NUMERIC, location TEXT )"
    )


# Function to execute SQL queries with a database connection
def execute_with_connection(query, attributes=None):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        if attributes is None:
            cur.execute(query)
        else:
            cur.execute(query, attributes)
        result = cur.fetchall()
        con.commit()
        con.close()
    except sqlite3.OperationalError:
        print("Query could not be executed")
        return None
    except sqlite3.Error:
        print("Connection to DB couldn't be established.")
        return None
    if result == []:
        result = None
    return result


# Function to insert temperature and humidity values into the database
def insert_values(degree, humidity, location):
    time_raw = datetime.datetime.now()
    timestamp = time_raw.strftime("%Y%m%d%H%M%S")
    execute_with_connection(
        f"INSERT INTO {TABLE_NAME} (degree, humidity, location, timestamp) VALUES (?, ?, ?, ?)",
        (degree, humidity, location, timestamp),
    )


# Function to get the maximum temperature from the preferred location
def get_max_temp(location):
    result = None
    if location is None:
        result = execute_with_connection(f"SELECT MAX(degree) FROM {TABLE_NAME}")
    else:
        result = execute_with_connection(
            f"SELECT MAX(degree) FROM {TABLE_NAME} WHERE location = ?", (location,)
        )
    if result is None:
        return None
    return result[0][0]


# Function to get the minimum temperature from the preferred location
def get_min_temp(location):
    result = None
    if location is None:
        result = execute_with_connection(f"SELECT MIN(degree) FROM {TABLE_NAME}")
    else:
        result = execute_with_connection(
            f"SELECT MIN(degree) FROM {TABLE_NAME} WHERE location = ?", (location,)
        )
    if result is None:
        return None
    return result[0][0]


# Function to get the latest temperature recorded from the preferred location
def get_latest_temp(location):
    result = None
    if location is None:
        result = execute_with_connection(
            f"SELECT degree FROM {TABLE_NAME} ORDER BY timestamp DESC LIMIT 1"
        )
    else:
        result = execute_with_connection(
            f"SELECT degree FROM {TABLE_NAME} WHERE location = ? ORDER BY timestamp DESC LIMIT 1",
            (location,),
        )
    if result is None:
        return None
    return result[0][0]


# Function to get the latest humidity recorded from the preferred location
def get_latest_humidity(location):
    result = None
    if location is None:
        result = execute_with_connection(
            f"SELECT humidity FROM {TABLE_NAME} ORDER BY timestamp DESC LIMIT 1"
        )
    else:
        result = execute_with_connection(
            f"SELECT humidity FROM {TABLE_NAME} WHERE location = ? ORDER BY timestamp DESC LIMIT 1",
            (location,),
        )
    if result is None:
        return None
    return result[0][0]


if __name__ == "__main__":
    setup()
