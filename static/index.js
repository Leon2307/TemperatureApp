const ipAdress = "172.20.49.44";
const port = 5000;
const cities = ["Mikkeli", "Helsinki"];

document.addEventListener("DOMContentLoaded", (event) => {
  for (city of cities) {
    let row = document.getElementById("weather-card-row");
    row.innerHTML += `
      <div class="col-md-7 mx-auto pb-2">
        <div class="weather-card">
          <img
            src="static/cloudy.png"
            alt="Weather Icon"
            class="weather-icon"
          />
          <h1 id="name-${city}" class="fw-bold text-light">${city}</h1>
          <div class="row mt-4">
            <div class="col-md-6 text-light">
              Temperature
              <p id="temp-${city}" class="fs-1 text-light">0°C</p>
            </div>
            <div class="col-md-6 text-light">
              Humidity
              <p id="humidity-${city}" class="fs-1 text-light">0%</p>
            </div>
          </div>
        </div>
      </div>`;
  }
  setInterval(setValues, 2000);
});

const setValues = async () => {
  for (city of cities) {
    let cityNameElement = document.getElementById(`name-${city}`);
    cityNameElement.textContent = city;

    let tempElement = document.getElementById(`temp-${city}`);
    let humidityElement = document.getElementById(`humidity-${city}`);

    fetch(`http://${ipAdress}:${port}/currentTemperature?location=${city}`)
      .then((res) => res.json())
      .then((data) => {
        let temp = "-";
        try {
          temp = data.temperature_degree;
        } catch {
          temp = "-";
          console.log("Temperature not in JSON");
        }
        tempElement.textContent = temp + "°C";
      });

    fetch(`http://${ipAdress}:${port}/currentHumidity?location=${city}`)
      .then((res) => res.json())
      .then((data) => {
        let humidity = "-";
        try {
          humidity = data.current_humidity;
        } catch {
          humidity = "-";
          console.log("Humidity not in JSON");
        }
        humidityElement.textContent = humidity + "%";
      });
  }
};
