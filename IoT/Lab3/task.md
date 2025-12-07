NATS protocol testing
Task: NATS same as MQTT is protocol used for messaging between different network nodes.
Almost all IoT devices are using IP protool for communication and MQTT or NATS is running on
top of IP layer
Same as MQTT, NATS can perform communication, the difference is that NATS does not have
intermediate server – known as “Broker” in MQTT topology
NATS communication happens directly “Server”, “Client” way without intermediate service as
MQTT Broker.
The task aim is to try individually run NATS server and prepare a basic NATS
subscriber, publisher scheme. The following examples can be used to run NATS on Windows or
Linux and
Python example is provided below:
1. Information how to run NATS under Linux or Windows
https://docs.nats.io/release-notes/whats_new/whats_new_210
https://github.com/nats-io/natscli/releases/tag/v0.1.0
2. Try basic python example for NATS communication
https://natsbyexample.com/examples/messaging/pub-sub/python
3. Prepare messaging output as summary for the work