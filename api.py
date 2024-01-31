from flask import Flask, render_template, request
from database import get_latest_temp, get_max_temp, get_min_temp, get_latest_humidity

app = Flask(__name__)


# Get Website
@app.route("/")
def main():
    return render_template("index.html")


# Get current temperature (e.g. /currentTemperature?location=Mikkeli)
@app.get("/currentTemperature")
def current_temp():
    location = request.args.get("location")
    latest_temp = get_latest_temp(location)
    if latest_temp is None:
        return '{"temperature_degree": null, "temperature_fahrenheit": null}'
    temp_degree = float(latest_temp)
    temp_fahrenheit = 1.8 * temp_degree + 3.0
    temp_json = f'{{"temperature_degree":{temp_degree}, "temperature_fahrenheit":{temp_fahrenheit}}}'
    return temp_json


# Get max temperature (e.g. /maxTemperature?location=Mikkeli)
@app.get("/maxTemperature")
def max_temp():
    location = request.args.get("location")
    max_temp = get_max_temp(location)
    if max_temp is None:
        return '{"temperature_degree": null, "temperature_fahrenheit": null}'
    max_temp_degree = float(max_temp)
    max_temp_fahrenheit = 1.8 * max_temp_degree + 32
    max_temp_json = f'{{"temperature_degree":{max_temp_degree}, "temperature_fahrenheit":{max_temp_fahrenheit}}}'
    return max_temp_json


# Get min temperature (e.g. /minTemperature?location=Mikkeli)
@app.get("/minTemperature")
def min_temp():
    location = request.args.get("location")
    min_temp = get_min_temp(location)
    if min_temp is None:
        return '{"temperature_degree": null, "temperature_fahrenheit": null}'
    min_temp_degree = float(min_temp)
    min_temp_fahrenheit = 1.8 * min_temp_degree + 32
    min_temp_json = f'{{"temperature_degree":{min_temp_degree}, "temperature_fahrenheit":{min_temp_fahrenheit}}}'
    return min_temp_json


# Get current humidity (e.g. /currentHumidity?location=Mikkeli)
@app.get("/currentHumidity")
def current_humidity():
    location = request.args.get("location")
    latest_humidity = get_latest_humidity(location)
    if latest_humidity is None:
        return '{"temperature_degree": null, "temperature_fahrenheit": null}'
    current_humidity = int(latest_humidity)
    current_humidity_json = f'{{"current_humidity":{current_humidity}}}'
    return current_humidity_json


if __name__ == "__main__":
    app.run("0.0.0.0")
