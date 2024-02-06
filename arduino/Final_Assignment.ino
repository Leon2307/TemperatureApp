// DHT - MQTT - Wifi
// This contains only temperature. Humidity is not used.

#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include <string.h>

// Wifi settings
const char* ssid = "MB210-G";
const char* password = "studentMAMK";

// MQTT Server IP address
const char* mqtt_server = "172.20.49.44";

// WiFi client
WiFiClient espClient;
// MQTT client
PubSubClient mqttClient(espClient);

// DHT sensor settings
#define DHTPIN 26
#define DHTTYPE DHT11 

DHT dht(DHTPIN, DHTTYPE);

/* Variables for tracking the measurements for average calculation */
int amountOfMeasurements = 5;
int measurementCounter = 0;

int amountOfMeasurementsHum = 5;
int measurementCounterHum = 0;
/* Measurements array */
float measurements[] = {0.0, 0.0, 0.0, 0.0, 0.0};
float measurementsHum[] = {0.0, 0.0, 0.0, 0.0, 0.0};

// Application setup
void setup() {
  // Serial
  Serial.begin(115200);
  // DHT temperature sensor
  dht.begin();
  // WiFi connection
  setup_wifi();
  // MQTT
  mqttClient.setServer(mqtt_server, 1883);

  Serial.println("Using array for calculating the sliding average.");
}

// WiFi connection
void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to WiFi SSID: ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

// MQTT connection
void reconnect() {
  // Loop until we're reconnected
  while (!mqttClient.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (mqttClient.connect("ESP32_Client")) {
      Serial.println("connected");
    } 
    else {
      Serial.print("failed, rc=");
      Serial.print(mqttClient.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

/* Function that is used to add or update new measurement in the list */
void addMeasurement(float temperature) {
	measurements[measurementCounter] = temperature;
	/* Update position */
	measurementCounter += 1;
  	/* Start again from the first item is the array is full */
	if (measurementCounter == amountOfMeasurements) {
		measurementCounter = 0;
	}
}

void addMeasurementHum(float humidity) {
	measurementsHum[measurementCounterHum] = humidity;
	/* Update position */
	measurementCounterHum += 1;
  	/* Start again from the first item is the array is full */
	if (measurementCounterHum == amountOfMeasurementsHum) {
		measurementCounterHum = 0;
	}
}
/* Function to calculate the average of measured temperatures */
float calculateAverage() {
	float avgTemp = 0.0;
	for (int counter = 0 ; counter < amountOfMeasurements ; counter++) {
		avgTemp += measurements[counter];
	}
	/* Calculate the average temp */
	avgTemp = avgTemp / amountOfMeasurements;
	return(avgTemp);
}

float calculateAverageHum() {
	float avgHum = 0.0;
	for (int counter = 0 ; counter < amountOfMeasurementsHum ; counter++) {
		avgHum += measurementsHum[counter];
	}
	/* Calculate the average temp */
	avgHum = avgHum / amountOfMeasurementsHum;
	return(avgHum);
}

// Application main loop
void loop() {
  // Reconnect mqtt if connection has been lost
  if (!mqttClient.connected()) {
    reconnect();
  }

  // Variable for measured temperature
  float measuredTemp = 0.0;
  float measuredHum = 0.0;

  // Read temperature from sensor
  measuredTemp = dht.readTemperature();
  measuredHum = dht.readHumidity();

  // Print measured temperature to serial console
  Serial.print("Temperature: ");
  Serial.print(measuredTemp);
  Serial.println("°C");

  // Print measured humidity to serial console
  Serial.print("Humidity: ");
  Serial.print(measuredHum);
  Serial.println("%");

  // Variable for average temperature/humidity
  float averageTemp = 0.0;
  float averageHum = 0.0;

  // Add measurement to list, calculate average temp and send it to mqtt
  addMeasurement(measuredTemp);
  averageTemp = calculateAverage();

  // Add measurement to list, calculate average humidity and send it to mqtt
  addMeasurementHum(measuredHum);
  averageHum = calculateAverageHum();

  // Print measured temperature to serial console
  Serial.print("Average Temperature(array used): ");
  Serial.println(averageTemp);

  // Print measured humidity to serial console
  Serial.print("Average Humidity(array used): ");
  Serial.println(averageHum);

  // Convert the average temperature value to a char array and publish it to MQTT
  String x = "{\"temperature\": " + String(averageTemp) + ", \"humidity\": " + String(averageHum) + ", \"location\": \"Mikkeli\"}";
  
  int len = x.length() + 1;
  char tempstring[len];
  x.toCharArray(tempstring, len);
  Serial.println(x);
  mqttClient.publish("weather/mikkeli", tempstring);


  // Sleep X seconds before next measurement
  sleep(2);
}