import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from matplotlib.pyplot import text

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
   

    def receive(self, text_data):
        # print(text_data)
        message = text_data
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )

    def chat_message(self, event):
        # print(event['message'])
        message = event['message']
        # message = json.loads(message)
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))

# if __name__ == "__main__":
#     from channels.layers import get_channel_layer
#     from asgiref.sync import async_to_sync
#     message = " to deploy"
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         'test',
#         {'type': 'chat_message', 'message': message}
#     )