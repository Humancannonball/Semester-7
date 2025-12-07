# Project 2: Home Assistant Mock Device Integration

## Overview
This project creates a mock IoT device that connects to Home Assistant via MQTT Discovery protocol, sending simulated temperature, humidity, and pressure data.

## Requirements
- Python 3.10+
- Docker (for MQTT broker and Home Assistant)
- paho-mqtt library

## Setup

### 1. Install Dependencies
```bash
pip install paho-mqtt
```

### 2. Start MQTT Broker
```bash
docker run -d --name mosquitto -p 1883:1883 eclipse-mosquitto:latest mosquitto -c /mosquitto-no-auth.conf
```

### 3. Start Home Assistant (Optional - for full demo)
```bash
docker run -d --name homeassistant \
  -p 8123:8123 \
  -v ha_config:/config \
  homeassistant/home-assistant:stable
```

Wait ~2 minutes for HA to start, then open http://localhost:8123

#### Configure MQTT in Home Assistant:
1. Go to Settings → Devices & Services
2. Click "+ Add Integration"
3. Search for "MQTT"
4. Enter broker: `host.docker.internal` (or your host IP)
5. Port: 1883
6. No username/password needed

---

## Running the Mock Device

### Option A: Test without Home Assistant

Terminal 1 - Start subscriber:
```bash
cd src
python mqtt_subscriber.py
```

Terminal 2 - Start mock device:
```bash
cd src
python mock_device.py
```

**Expected output (Terminal 1):**
```
[homeassistant/sensor/mock_sensor_01_temp/config]
{
  "name": "Temperature",
  "device_class": "temperature",
  ...
}
[home/mock_sensor_01/temperature]
{"value": 23.5}
```

📸 **Screenshot:** Take screenshot showing discovery config and sensor data.

---

### Option B: Full Home Assistant Integration

1. Start Mosquitto broker (see Setup step 2)
2. Start Home Assistant (see Setup step 3)
3. Configure MQTT integration in HA
4. Run mock device:
```bash
cd src
python mock_device.py
```

5. In Home Assistant:
   - Go to Settings → Devices & Services → MQTT
   - You should see "Mock Weather Station" device
   - Click on it to see Temperature, Humidity, Pressure entities
   - Values update every 5 seconds

📸 **Screenshot:** Take screenshot of Home Assistant showing the mock device with sensor values.

---

## How It Works

### MQTT Discovery
The mock device publishes configuration to:
- `homeassistant/sensor/mock_sensor_01_temp/config`
- `homeassistant/sensor/mock_sensor_01_humidity/config`
- `homeassistant/sensor/mock_sensor_01_pressure/config`

Home Assistant automatically discovers and creates entities.

### Sensor Data
Random values are published every 5 seconds to:
- `home/mock_sensor_01/temperature`
- `home/mock_sensor_01/humidity`
- `home/mock_sensor_01/pressure`

---

## Cleanup
```bash
docker stop mosquitto homeassistant
docker rm mosquitto homeassistant
docker volume rm ha_config
```
