# Project 1: Django and MQTT

## Overview
This project demonstrates Django web framework with WebSocket support and MQTT integration.

## Requirements
- Python 3.10+
- Docker (for MQTT broker)
- MQTTx client (optional, for testing)

## Setup

### 1. Install Dependencies
```bash
cd "IoT/Django and MQTT project #1/src/django_mqtt"
pip install django channels daphne paho-mqtt requests
```

### 2. Start MQTT Broker (Mosquitto)
```bash
docker run -d --name mosquitto -p 1883:1883 eclipse-mosquitto:latest mosquitto -c /mosquitto-no-auth.conf
```

---

## Task 1.1: Basic Django Server

### Run
```bash
cd src/django_mqtt
python manage.py runserver
```

### Test
Open browser: http://127.0.0.1:8000/

**Expected output:** "Django MQTT Server - Server is running!"

📸 **Screenshot:** Take screenshot of browser showing the message.

---

## Task 1.2: WebSocket Example

### Run (uses Daphne ASGI server)
```bash
cd src/django_mqtt
daphne -b 127.0.0.1 -p 8000 django_mqtt.asgi:application
```

### Test
Open browser: http://127.0.0.1:8000/ws-test/

1. You should see "Connected to WebSocket" message
2. Type a message and click Send
3. Server echoes back the message

📸 **Screenshot:** Take screenshot showing sent messages and echo responses.

---

## Task 1.3: MQTT Listener

### Run
Terminal 1 - Start MQTT listener:
```bash
cd src/django_mqtt
python manage.py mqtt_listener
```

Terminal 2 - Send test message (or use MQTTx):
```bash
docker exec mosquitto mosquitto_pub -t "test/topic" -m "Hello from MQTTx!"
```

**Expected output in Terminal 1:**
```
Connected to MQTT broker (code: 0)
Subscribed to all topics (#)
Waiting for messages from MQTTx...
[test/topic] Hello from MQTTx!
```

📸 **Screenshot:** Take screenshot of terminal showing received MQTT messages.

---

## Task 2: API to MQTT

### Run
```bash
cd src
python api_fetch.py
```

**Expected output:**
```
Fetching weather data for Vilnius...
Data saved to output.json
Connected to MQTT broker (code: 0)
Published to weather/data: {"city": "Vilnius", "temperature_c": "2", ...}
Done!
```

### Verify output.json
```bash
cat output.json | head -20
```

📸 **Screenshot:** Take screenshot of terminal output and output.json content.

---

## Cleanup
```bash
docker stop mosquitto
docker rm mosquitto
```
