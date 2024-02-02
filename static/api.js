const ipAdress = "0.0.0.0";
const port = "5000";

const api = {
  methods: [
    {
      type: "GET",
      name: "Current Temperature",
      link: `http://${ipAdress}:${port}/currentTemperature?location=Mikkeli`,
      result:
        '{ <br/> "temperature_degree": 30.23, <br />"temperature_fahrenheit": 90.45 <br />}',
    },
    {
      type: "GET",
      name: "Maximum Temperature",
      link: `http://${ipAdress}:${port}/maxTemperature?location=Mikkeli`,
      result:
        '{ <br/> "temperature_degree": 30.23, <br />"temperature_fahrenheit": 90.45 <br />}',
    },
    {
      type: "GET",
      name: "Minimum Temperature",
      link: `http://${ipAdress}:${port}/minTemperature?location=Mikkeli`,
      result:
        '{ <br/> "temperature_degree": 30.23, <br />"temperature_fahrenheit": 90.45 <br />}',
    },
    {
      type: "GET",
      name: "Current Humidity",
      link: `http://${ipAdress}:${port}/currentHumidity?location=Mikkeli`,
      result: '{ <br/> "current_humidity": 40 <br />}',
    },
  ],
};

document.addEventListener("DOMContentLoaded", (event) => {
  for (method of api.methods) {
    buildAPICard(method);
  }
});

const buildAPICard = (method) => {
  let container = document.getElementById('card-container');
  container.innerHTML += `
    <!-- API card -->
    <div class="col-md-6 offset-md-3 mb-2">
    <div class="card transparent rounded-4 api-card">
      <div class="card-body">
        <div class="d-flex">
          <div class="text-success fw-bold fs-3 pe-2">GET</div>
          <div class="fw-bold fs-3 text-light">${method.name}</div>
        </div>
        <p class="text-success">
          ${method.link}
        </p>
        <code class="text-light">
          ${method.result}
        </code>
      </div>
    </div>
    </div>
    <!-- End API card-->`;
};
