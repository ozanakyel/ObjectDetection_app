import websocket 

class WebSocket(object):
    def __init__(self):
        self.ws = websocket.create_connection("ws://127.0.0.1:8000/ws/socket-server/")
    
    def send(self, message):
        self.ws.send(message)