#!/usr/bin/env python3
"""
Simple MQTT subscriber to verify mock device messages.
Use this to test without Home Assistant.
"""

import json
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected to MQTT broker (code: {rc})")
    # Subscribe to all home assistant and device topics
    client.subscribe("homeassistant/#")
    client.subscribe("home/#")
    print("Subscribed to homeassistant/# and home/#")
    print("Waiting for messages...\n")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"[{msg.topic}]")
        print(json.dumps(payload, indent=2))
        print("-" * 40)
    except json.JSONDecodeError:
        print(f"[{msg.topic}] {msg.payload.decode()}")
        print("-" * 40)

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nDisconnecting...")
        client.disconnect()

if __name__ == "__main__":
    main()
