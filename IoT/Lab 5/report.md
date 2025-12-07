# Lab 5: MQTT and Home Assistant Integration

## Objective
Set up MQTT communication using paho-mqtt library with a broker.

## Setup
For simplicity, we use Eclipse Mosquitto MQTT broker in Docker instead of full Home Assistant.

### Start MQTT Broker
```bash
docker run -d --name mosquitto -p 1883:1883 eclipse-mosquitto:latest mosquitto -c /mosquitto-no-auth.conf
```

### Install Python Library
```bash
pip install paho-mqtt
```

## Implementation

### subscriber.py
```python
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")
    client.subscribe("iot/#")

def on_message(client, userdata, msg):
    print(f"Received: {msg.topic} -> {msg.payload.decode()}")

if __name__ == "__main__":
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect("localhost", 1883, 60)
    
    print("Subscriber listening on 'iot/#'...")
    client.loop_forever()
```

### publisher.py
```python
import paho.mqtt.client as mqtt
import time
import json

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")

if __name__ == "__main__":
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    
    client.connect("localhost", 1883, 60)
    client.loop_start()
    
    time.sleep(1)
    
    messages = [
        {"topic": "iot/temperature", "data": {"value": 25.5, "unit": "C"}},
        {"topic": "iot/humidity", "data": {"value": 60, "unit": "%"}},
        {"topic": "iot/pressure", "data": {"value": 1013, "unit": "hPa"}},
    ]
    
    for msg in messages:
        payload = json.dumps(msg["data"])
        client.publish(msg["topic"], payload)
        print(f"Published to {msg['topic']}: {payload}")
        time.sleep(0.5)
    
    client.disconnect()
    client.loop_stop()
    print("Done publishing")
```

## Running

1. Start Mosquitto broker (Docker)
2. Run subscriber: `python subscriber.py &`
3. Run publisher: `python publisher.py`

## Output
```
Subscriber listening on 'iot/#'...
Connected with result code Success
Connected with result code Success
Published to iot/temperature: {"value": 25.5, "unit": "C"}
Received: iot/temperature -> {"value": 25.5, "unit": "C"}
Published to iot/humidity: {"value": 60, "unit": "%"}
Received: iot/humidity -> {"value": 60, "unit": "%"}
Published to iot/pressure: {"value": 1013, "unit": "hPa"}
Received: iot/pressure -> {"value": 1013, "unit": "hPa"}
Done publishing
```

## Conclusion
MQTT provides a lightweight pub/sub messaging protocol ideal for IoT devices. The paho-mqtt library makes it easy to create Python clients. The subscriber uses wildcard topic `iot/#` to receive all messages under that prefix.

### Note on Home Assistant
For full Home Assistant integration, install HA via Docker:
```bash
docker run -d --name homeassistant -p 8123:8123 homeassistant/home-assistant:stable
```
Then configure MQTT integration in HA settings and use credentials in the Python client.
