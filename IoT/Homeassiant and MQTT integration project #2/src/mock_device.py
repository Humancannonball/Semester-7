#!/usr/bin/env python3
"""
Mock IoT device that publishes sensor data to Home Assistant via MQTT Discovery.
Simulates temperature, humidity, and pressure sensors.
"""

import json
import time
import random
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
DEVICE_ID = "mock_sensor_01"
DEVICE_NAME = "Mock Weather Station"

# MQTT Discovery topics (Home Assistant auto-discovery)
DISCOVERY_PREFIX = "homeassistant"

# Sensor configurations
SENSORS = [
    {
        "name": "Temperature",
        "unique_id": f"{DEVICE_ID}_temp",
        "device_class": "temperature",
        "unit_of_measurement": "°C",
        "state_topic": f"home/{DEVICE_ID}/temperature",
        "value_template": "{{ value_json.value }}",
    },
    {
        "name": "Humidity",
        "unique_id": f"{DEVICE_ID}_humidity",
        "device_class": "humidity",
        "unit_of_measurement": "%",
        "state_topic": f"home/{DEVICE_ID}/humidity",
        "value_template": "{{ value_json.value }}",
    },
    {
        "name": "Pressure",
        "unique_id": f"{DEVICE_ID}_pressure",
        "device_class": "pressure",
        "unit_of_measurement": "hPa",
        "state_topic": f"home/{DEVICE_ID}/pressure",
        "value_template": "{{ value_json.value }}",
    },
]

def publish_discovery_config(client):
    """Publish MQTT discovery config for Home Assistant"""
    device_info = {
        "identifiers": [DEVICE_ID],
        "name": DEVICE_NAME,
        "model": "Virtual Sensor v1.0",
        "manufacturer": "IoT Lab",
    }
    
    for sensor in SENSORS:
        config_topic = f"{DISCOVERY_PREFIX}/sensor/{sensor['unique_id']}/config"
        config_payload = {
            "name": sensor["name"],
            "unique_id": sensor["unique_id"],
            "device_class": sensor["device_class"],
            "unit_of_measurement": sensor["unit_of_measurement"],
            "state_topic": sensor["state_topic"],
            "value_template": sensor["value_template"],
            "device": device_info,
        }
        client.publish(config_topic, json.dumps(config_payload), retain=True)
        print(f"Published discovery config for {sensor['name']}")

def generate_sensor_data():
    """Generate random sensor values"""
    return {
        "temperature": round(random.uniform(18.0, 28.0), 1),
        "humidity": round(random.uniform(40.0, 80.0), 1),
        "pressure": round(random.uniform(1000, 1025), 1),
    }

def publish_sensor_data(client, data):
    """Publish sensor data to state topics"""
    for sensor_type, value in data.items():
        topic = f"home/{DEVICE_ID}/{sensor_type}"
        payload = json.dumps({"value": value})
        client.publish(topic, payload)
        print(f"Published {sensor_type}: {value}")

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    
    def on_connect(client, userdata, flags, rc, properties=None):
        print(f"Connected to MQTT broker at {MQTT_BROKER}:{MQTT_PORT}")
        # Publish discovery configs on connect
        publish_discovery_config(client)
    
    client.on_connect = on_connect
    
    print(f"Connecting to MQTT broker...")
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    
    time.sleep(2)  # Wait for connection and discovery
    
    print("\nStarting sensor data publishing (Ctrl+C to stop)...")
    print("-" * 50)
    
    try:
        while True:
            data = generate_sensor_data()
            publish_sensor_data(client, data)
            print("-" * 50)
            time.sleep(5)  # Publish every 5 seconds
    except KeyboardInterrupt:
        print("\nStopping mock device...")
        client.disconnect()
        client.loop_stop()

if __name__ == "__main__":
    main()
