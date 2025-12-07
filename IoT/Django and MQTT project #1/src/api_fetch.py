#!/usr/bin/env python3
"""
Fetches weather data from wttr.in API, saves to output.json,
and publishes to MQTT broker.
"""

import json
import requests
import paho.mqtt.client as mqtt
import time

CITY = "Vilnius"
API_URL = f"https://wttr.in/{CITY}?format=j1"
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "weather/data"

def fetch_weather():
    """Fetch weather data from wttr.in API"""
    print(f"Fetching weather data for {CITY}...")
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()

def save_to_file(data, filename="output.json"):
    """Save data to JSON file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {filename}")

def publish_to_mqtt(data):
    """Publish data to MQTT broker"""
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    
    def on_connect(client, userdata, flags, rc, properties=None):
        print(f"Connected to MQTT broker (code: {rc})")
    
    client.on_connect = on_connect
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    time.sleep(1)
    
    # Extract key weather info
    current = data.get('current_condition', [{}])[0]
    weather_info = {
        'city': CITY,
        'temperature_c': current.get('temp_C'),
        'humidity': current.get('humidity'),
        'pressure': current.get('pressure'),
        'weather_desc': current.get('weatherDesc', [{}])[0].get('value'),
        'wind_speed_kmph': current.get('windspeedKmph'),
    }
    
    payload = json.dumps(weather_info)
    client.publish(MQTT_TOPIC, payload)
    print(f"Published to {MQTT_TOPIC}: {payload}")
    
    client.disconnect()
    client.loop_stop()

def main():
    try:
        # Fetch data from API
        data = fetch_weather()
        
        # Save to file
        save_to_file(data)
        
        # Publish to MQTT
        publish_to_mqtt(data)
        
        print("\nDone!")
        
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
