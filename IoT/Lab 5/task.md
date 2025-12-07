MQTT and Home Assistant integration
1.2.3.Prepare/Setup Home Assistant follow official website
Create python MQTT client, that would be able to communicate withį HA platform
Before usage below example, install required packages pip3 install paho-mqtt ir pip3
install json
Example code for HA:
1. Replace broker_address with your own
2. Install a fully separate HA platform
import paho.mqtt.client as mqtt
import time
import json
def connect_broker(broker_address, client_name):
client = mqtt.Client(client_name)
client.username_pw_set("mqtt", "mqtt")
client.connect(broker_address, 1883)
time.sleep(1)
client.loop_start()
return client
if __name__ == "__main__":
server = "homeassistant.local"
client_name = "tester_ha"
client = connect_broker(server, client_name)
try:
while True:
message = input('Send some message: ')
topic = input('Specify the topic: ')
client.publish(topic, message)
except KeyboardInterrupt:
client.disconnect()
client.loop_stop()