import sqlite3

DB_NAME = "temperatureApp.db"
TABLE_NAME = "temperature"

# Create Database and Table
def setup():
    execute_with_connection(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( id INTEGER PRIMARY KEY AUTOINCREMENT, degree REAL, humidity REAL, timestamp NUMERIC, location TEXT )')


def execute_with_connection(query, attributes=None):
    try:
        con = sqlite3.connect(DB_NAME)
    except:
        print("Connection to DB couldn't be established.")
    cur = con.cursor()
    if attributes is None:
        cur.execute(query)
    else:
        cur.execute(query, attributes)
    con.commit()
    con.close()

# def get_max_temp(Location=None):​

# def get_min_temp(Location=None):​

# def get_latest_temp(Location):​

# def get_latest_humidity(Location):​

def insert_values(degree, humidity, location):
    


if __name__ == '__main__':
    setup()


