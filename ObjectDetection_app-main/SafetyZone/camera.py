import os
from cv2 import cv2
import numpy as np
from django.conf import settings
from SafetyZone import object_detector
# from SafetyZone.object_detection import object_detection_folder_onnxTF2
from .isIn import check_rois
from .draw_poly import draw_poly, draw_poly_, show_ok_nok
import logging
from threading import Thread
import time

from django.shortcuts import render
from .models import *
# from .log_functions import *
import cv2
import threading
import asyncio
from SafetyZone import rois 
# from .plc import Plc

from SafetyZone.models import Project, Config, ProjectConfig

import websocket 

class WebSocket(object):
    def __init__(self):
        self.ws = websocket.create_connection("ws://127.0.0.1:8081/ws/socket-server/")
    
    def send(self, message):
        self.ws.send(message)

web_socket = WebSocket()
# configs = ProjectConfig.objects.filter(projectID_id = 1).values()
# imageSaveLocation = configs[49]['configValue']
# serverLogLocation = configs[45]['configValue']

# PLC = Plc('10.15.221.254', PlcRack=0, PlcSlot=1)
# PLC2 = Plc('10.15.221.254', PlcRack=0, PlcSlot=1)
# PLC3 = Plc('10.15.221.254', PlcRack=0, PlcSlot=1)

# threading.Thread(target=PLC.Read_Bit, args=(90, 4, 0, 0.0275), daemon=True).start()
# threading.Thread(target=PLC2.Read_Bit, args=(90, 4, 1, 0.0275), daemon=True).start()

rois_path = r'C:\Users\Harun\Desktop\ObjectDetection_app\SafetyZone\rois.json'
class_id, poly_point_list, is_object_have, reverse = rois.get_rois(rois_path)
#to capture video class

class VideoCamera(object):
    def __init__(self):
        # self.video = cv2.VideoCapture('rtsp://admin:Abc1234*@10.16.222.253/')
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=(), daemon=True).start()
        self.detect = object_detector.ObjectDetection()
        # self.detect.setDaemon(True)
        self.start_time = time.time()
        self.display_time = 1
        self.fc = 0
        self.FPS = 0

    def __del__(self):
        self.video.release()

    def get_frame(self, method):
        image = self.frame
        self.fc+=1
        TIME = time.time() - self.start_time
        
        if (TIME) >= self.display_time :
            self.FPS = self.fc / (TIME)
            self.fc = 0
            self.start_time = time.time()

        fps_disp = "FPS: "+str(self.FPS)[:5]
        
        # Add FPS count on frame
        # web_socket.send(fps_disp)
        image = cv2.putText(image, fps_disp, (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        _, jpeg = cv2.imencode('.jpg', image)
        image_detected, isIn, boxes, scores, classes = self.detect.object_detection(image)
        image_detected = draw_polly_and_check_isin(image_detected, boxes, scores, classes, isIn , method)

        _, image = cv2.imencode('.jpg', image_detected)
        return jpeg.tobytes(), image.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame,_ = camera.get_frame("ORJ")
    
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
# def gen2(camera):
#     _, frame = camera.get_frame("DETECTION")
#     while True:
#         if PLC.bit_value == True:
#             time.sleep(0.0275)
#             _, frame = camera.get_frame("DETECTION")
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#         else:
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen2(camera):
    while True:
        _, frame= camera.get_frame("DETECTION")
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def draw_polly_and_check_isin(image, boxes, scores, classes, isIn, method):
    result = None
    # RoiAlign = ProjectConfig.objects.filter(configKeyID_id = 53).values()
    boxes = np.squeeze(boxes)
    scores = np.squeeze(scores)
    classes = np.squeeze(classes).astype(np.int32)
    x = image.shape[0]
    y = image.shape[1]
    # TODO Roi sayisina gore total result dondurulecek sekilde revize edilecek.
    draw_isIn = False
    for polly_point in poly_point_list:
        draw_poly_(image, polly_point)
    polly_is_in = []
    for i in range(min(12, boxes.shape[0])):
        if scores is None or scores[i] > 0.7:
            box = tuple(boxes[i].tolist())
            
            for index, polly_point in enumerate(poly_point_list):
                if int(classes[i]) == int(class_id[index]):
                    isIn = check_rois(image, polly_point, box, "middlecenter")

                    # if len(polly_is_in) == 2:
                    #     polly_is_in.pop(0)
                    #     polly_is_in.pop(1)
                    if isIn == True:
                        draw_isIn = isIn
                        polly_is_in.append(str(draw_isIn))
                    else:
                        polly_is_in.append(str(draw_isIn))

                    image = draw_poly(image, polly_point, draw_isIn)
    image = show_ok_nok(image, draw_isIn)
    message = []
    message.append({"IsIn" : str(draw_isIn), "PollyIsIn": polly_is_in})
    web_socket.send(str(message))


            # isIn = check_rois(image, poly_point_list[0], box, RoiAlign[0]['configValue'])

    # print(isIn)
    # if isIn != PLC2.bit_value:
    #     if method == "DETECTION":
    #         if isIn!= None:
    #             PLC3.Set_bit(DB=90, DBX=4, DB_X=1, value=isIn)
    #         else:
    #             pass
    return image

