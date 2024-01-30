from flask import Flask, render_template, request
from database import get_current_temp, get_max_temp, get_min_temp, get_current_humidity

app = Flask(__name__)


# Get Website
@app.route("/")
def main():
    return render_template("index.html")


# Get current temperature (e.g. /currentTemperature?location="Mikkeli")
@app.get("/currentTemperature")
def current_temp():
    location = request.args.get("location")
    temp_degree = get_current_temp(location)
    temp_fahrenheit = 1.8 * temp_degree + 3
    temp_json = f'\{"temperature_degree":{temp_degree}, "temperature_fahrenheit":{temp_fahrenheit}\}'
    return temp_json


# Get max temperature (e.g. /maxTemperature?location="Mikkeli")
@app.get("/maxTemperature")
def max_temp():
    location = request.args.get("location")
    max_temp_degree = get_max_temp(location)
    max_temp_fahrenheit = 1.8 * max_temp_degree +32
    max_temp_json = f'\{"temperature_degree":{max_temp_degree}, "temperature_fahrenheit":{max_temp_fahrenheit}\}'
    return max_temp_json

# Get min temperature (e.g. /minTemperature?location="Mikkeli")
@app.get("/minTemperature")
def min_temp():
    location = request.args.get("location")
    min_temp_degree = get_min_temp(location)
    min_temp_fahrenheit = 1.8 * min_temp_degree +32
    min_temp_json = f'\{"temperature_degree":{min_temp_degree}, "temperature_fahrenheit":{min_temp_fahrenheit}\}'
    return min_temp_json

# Get current humidity (e.g. /currentHumidity?location="Mikkeli")
@app.get("/currentHumidity")
def current_humidity():
    location = request.args.get("location")
    current_humidity = get_current_humidity(location)
    current_humidity_json = f'\{"current_humidity":{current_humidity}\}'
    return current_humidity_json

if __name__ == "__main__":
    app.run("0.0.0.0")
