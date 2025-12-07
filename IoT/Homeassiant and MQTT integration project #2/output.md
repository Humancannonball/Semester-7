[mark@markstation Semester 7]$ sleep 2 && cd "/home/mark/Documents/Semester 7/IoT/Homeassiant and MQTT integration project #2/src" && timeout 15 "/home/mark/Documents/Semester 7/.venv/bin/python" mock_device.py
Connecting to MQTT broker...
Connected to MQTT broker at localhost:1883
Published discovery config for Temperature
Published discovery config for Humidity
Published discovery config for Pressure
[homeassistant/sensor/mock_sensor_01_temp/config]
{
  "name": "Temperature",
  "unique_id": "mock_sensor_01_temp",
  "device_class": "temperature",
  "unit_of_measurement": "\u00b0C",
  "state_topic": "home/mock_sensor_01/temperature",
  "value_template": "{{ value_json.value }}",
  "device": {
    "identifiers": [
      "mock_sensor_01"
    ],
    "name": "Mock Weather Station",
    "model": "Virtual Sensor v1.0",
    "manufacturer": "IoT Lab"
  }
}
----------------------------------------
[homeassistant/sensor/mock_sensor_01_humidity/config]
{
  "name": "Humidity",
  "unique_id": "mock_sensor_01_humidity",
  "device_class": "humidity",
  "unit_of_measurement": "%",
  "state_topic": "home/mock_sensor_01/humidity",
  "value_template": "{{ value_json.value }}",
  "device": {
    "identifiers": [
      "mock_sensor_01"
    ],
    "name": "Mock Weather Station",
    "model": "Virtual Sensor v1.0",
    "manufacturer": "IoT Lab"
  }
}
----------------------------------------
[homeassistant/sensor/mock_sensor_01_pressure/config]
{
  "name": "Pressure",
  "unique_id": "mock_sensor_01_pressure",
  "device_class": "pressure",
  "unit_of_measurement": "hPa",
  "state_topic": "home/mock_sensor_01/pressure",
  "value_template": "{{ value_json.value }}",
  "device": {
    "identifiers": [
      "mock_sensor_01"
    ],
    "name": "Mock Weather Station",
    "model": "Virtual Sensor v1.0",
    "manufacturer": "IoT Lab"
  }
}
----------------------------------------

Starting sensor data publishing (Ctrl+C to stop)...
--------------------------------------------------
Published temperature: 25.5
Published humidity: 54.7
Published pressure: 1010.3
--------------------------------------------------
[home/mock_sensor_01/temperature]
{
  "value": 25.5
}
----------------------------------------
[home/mock_sensor_01/humidity]
{
  "value": 54.7
}
----------------------------------------
[home/mock_sensor_01/pressure]
{
  "value": 1010.3
}
----------------------------------------
Published temperature: 19.6
Published humidity: 64.5
Published pressure: 1006.3
--------------------------------------------------
[home/mock_sensor_01/temperature]
{
  "value": 19.6
}
----------------------------------------
[home/mock_sensor_01/humidity]
{
  "value": 64.5
}
----------------------------------------
[home/mock_sensor_01/pressure]
{
  "value": 1006.3
}
----------------------------------------
Published temperature: 24.8
Published humidity: 40.9
Published pressure: 1011.6
--------------------------------------------------
[home/mock_sensor_01/temperature]
{
  "value": 24.8
}
----------------------------------------
[home/mock_sensor_01/humidity]
{
  "value": 40.9
}
----------------------------------------
[home/mock_sensor_01/pressure]
{
  "value": 1011.6
}
----------------------------------------