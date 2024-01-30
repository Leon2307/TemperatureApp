from flask import Flask, render_template, request
from database import get_current_temp

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
    temp_fahrenheit = 1.8 * temp_degree + 32
    temp_json = f'"temperature_degree":{temp_degree}, "temperature_fahrenheit":{temp_fahrenheit}'
    return temp_json


# Get max temperature


# Get min temperature

# Get current humidity


if __name__ == "__main__":
    app.run("0.0.0.0")
