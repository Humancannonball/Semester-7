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
    
    # Publish sensor data
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
