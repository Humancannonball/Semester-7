import json
from channels.generic.websocket import WebsocketConsumer

class EchoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({'message': 'Connected to WebSocket!'}))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '')
        # Echo back the message
        self.send(text_data=json.dumps({
            'message': f'Echo: {message}'
        }))
