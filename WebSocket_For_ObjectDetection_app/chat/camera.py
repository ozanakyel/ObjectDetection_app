from cv2 import cv2
import threading
import datetime
# from channels.layers import get_channel_layer
# from .websocket_connection import WebSocket
# from asgiref.sync import async_to_sync
# from . import object_detector
# channel_layer = get_channel_layer()
class VideoCamera(object):
    def __init__(self):
        # self.video = cv2.VideoCapture('rtsp://admin:Abc1234*@10.16.222.253/')
        # self.video = cv2.VideoCapture('http://192.168.1.38:8081/video')
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=(), daemon=True).start()
        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send)(
        #     'test',
        #     {'type': 'chat_message', 'message': 'VideoCamera'}
        # )
        # self.detect = object_detector.ObjectDetection()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        # _, jpeg = cv2.imencode('.jpg', image)
        # image_detected, isIn, boxes, scores, classes = self.detect.object_detection(image)
        # # image_detected = draw_polly_and_check_isin(image_detected, boxes, scores, classes, isIn , method)
        # _, image = cv2.imencode('.jpg', image_detected)
        return image

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera, websocket):
    websocket.send("Kameradan Görüntü okundu")
    while True:
        frame = camera.get_frame()
        cv2.imshow('frame' , frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        # yield (b'--frame\r\n'
        #         b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r


import websocket 

class WebSocket(object):
    def __init__(self):
        self.ws = websocket.create_connection("ws://127.0.0.1:8000/ws/socket-server/")
    
    def send(self, message):
        self.ws.send(message)

if __name__ == "__main__":
    wssend = WebSocket()
    cam = VideoCamera()
    while True:
        frame = cam.get_frame()
        print(type(frame))
        # wssend.send(f'Kameradan Görüntü Okundu Tarih: {datetime.datetime.now()}')
        # wssend.send(frame)
        cv2.imshow('frame' , frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break