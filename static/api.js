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
  ],
};
