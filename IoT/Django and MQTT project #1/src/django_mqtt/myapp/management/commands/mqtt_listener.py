from django.core.management.base import BaseCommand
import paho.mqtt.client as mqtt

class Command(BaseCommand):
    help = 'Starts MQTT listener that prints messages from MQTTx'

    def handle(self, *args, **options):
        def on_connect(client, userdata, flags, rc, properties=None):
            self.stdout.write(self.style.SUCCESS(f'Connected to MQTT broker (code: {rc})'))
            client.subscribe('#')  # Subscribe to all topics
            self.stdout.write('Subscribed to all topics (#)')
            self.stdout.write('Waiting for messages from MQTTx...')

        def on_message(client, userdata, msg):
            self.stdout.write(
                self.style.WARNING(f'[{msg.topic}] ') + 
                f'{msg.payload.decode()}'
            )

        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.on_connect = on_connect
        client.on_message = on_message

        self.stdout.write('Connecting to MQTT broker at localhost:1883...')
        client.connect('localhost', 1883, 60)

        try:
            client.loop_forever()
        except KeyboardInterrupt:
            self.stdout.write(self.style.SUCCESS('MQTT listener stopped'))
            client.disconnect()
