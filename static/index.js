const ipAdress = "172.20.49.44";
const port = 5000;
const cities = ["Mikkeli"];

document.addEventListener("DOMContentLoaded", (event) => {
  setInterval(setValues, 3000);
});

const setValues = async () => {
  for (city of cities) {
    let cityNameElement = document.getElementById("city-1");
    cityNameElement.textContent = city;

    let tempElement = document.getElementById("temp");
    let humidityElement = document.getElementById("humidity");

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
