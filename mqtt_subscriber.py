from paho.mqtt import client as mqtt_client
from database import insert_values
import json


broker = '0.0.0.0'
port = 8080
topic = "weather/mikkeli"
client_id = 'subscribe-weather-station'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        msg_json = json.loads(msg)
        insert_values(msg_json["degree"], msg_json["humidity"], msg_json["location"])

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
