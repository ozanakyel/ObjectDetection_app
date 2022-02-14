import os,urllib.request
from cv2 import cv2
import numpy as np
from django.conf import settings
from SafetyZone import object_detector
# from SafetyZone.object_detection import object_detection_folder_onnxTF2
from .isIn import check_rois
import logging
from threading import Thread
import time

from django.shortcuts import render
from .models import *
import cv2
import threading
import datetime
from SafetyZone import rois 

from SafetyZone.models import Project, Config, ProjectConfig

# configs = ProjectConfig.objects.filter(projectID_id = 1).values()
# imageSaveLocation = configs[49]['configValue']
# serverLogLocation = configs[45]['configValue']

rois_path = "C:/Users/Harun/Desktop/ObjectDetection_app/SafetyZone/rois.json"
#to capture video class
class VideoCamera(object):
    def __init__(self):
        # self.video = cv2.VideoCapture('http://192.168.1.38:8081/video')
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=(), daemon=True).start()
        self.detect = object_detector.ObjectDetection()
        # self.detect.setDaemon(True)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        image_orj = image.copy()
        _, jpeg = cv2.imencode('.jpg', image)
        image_detected, isIn, boxes, scores, classes = self.detect.object_detection(image)
        image_detected = draw_polly_and_check_isin(image_detected, boxes, scores, classes, isIn)
        _, image = cv2.imencode('.jpg', image_detected)
        return jpeg.tobytes(),image.tobytes()

    # def get_box(self):
    #     self.detect.get_boxes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame,_ = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen2(camera):
    while True:
        _, frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def draw_polly_and_check_isin(image, boxes, scores, classes, isIn):
    class_id, poly_point_list, is_object_have, reverse = rois.get_rois(rois_path)
    # print(poly_point_list)
    pts = np.array(poly_point_list[0], np.int32)
    pts = pts.reshape((-1, 1, 2))
    isClosed = True
    # Blue color in BGR
    color = (255, 0, 0)
    # Line thickness of 2 px
    thickness = 2
    image = cv2.polylines(image, [pts], isClosed, color, thickness)

    boxes = np.squeeze(boxes)
    scores = np.squeeze(scores)
    classes = np.squeeze(classes).astype(np.int32)
    x = image.shape[0]
    y = image.shape[1]
    # print(pts)
    for i in range(min(1, boxes.shape[0])):
        if scores is None or scores[i] > 0.7:
            box = tuple(boxes[i].tolist())
            print(check_rois(image, poly_point_list[0], box, "middlecenter"))


























    #         startpoint = (int(y*box[1]), int(x*box[0]))
    #         endpoint = (int(y*box[3]), int(x*box[2]))
    #         # [[1900, 1079], [1900, 70], [150, 70], [150, 1079]]
    #         if ( startpoint[0] < 1900 and startpoint[0] > 150 and endpoint[0] < 1900 and endpoint[0] > 150 and startpoint[1] < 1081 and startpoint[1] > 70 and endpoint[1] < 1081 and endpoint[1] > 70):
    #             isIn = True
    #             if isIn == True:
    #                 image = cv2.putText(image, 'OK', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
    #         else:
    #             isIn = False
    #             if isIn == False:
    #                 image = cv2.putText(image, 'NOK', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    # if (isIn == True):
    #         image_name = str(datetime.datetime.now()).replace(" ", "_").replace(".",":") + '_detected' +'.jpg'
    #         image_name_orj = str(datetime.datetime.now()).replace(" ", "_").replace(".",":") +'.jpg'
    #         # cv2.imwrite(os.path.join(imageSaveLocation, image_name_orj), image_orj)
    #         # cv2.imwrite(os.path.join(imageSaveLocation, image_name), image_detected)
    #         # print(os.path.join(configs[50]['configValue'], image_name), 'olarak kaydedildi')
    #         path = str(datetime.date.today()) + '.txt'
    #         direction =  os.path.join(str(serverLogLocation), path)
    #         if not os.path.exists(direction):
    #             with open( direction , 'w+') as f:
    #                 f.write(str(os.path.join(imageSaveLocation, image_name_orj)) + ' olarak kaydedildi')
    #                 f.write('\n')
    #                 f.write(str(os.path.join(imageSaveLocation, image_name)) + ' olarak kaydedildi')
    #                 f.write('\n')
    #                 f.close()
    #         else:
    #             with open( direction , 'a') as f:
    #                 f.write(str(os.path.join(imageSaveLocation, image_name_orj)) + ' olarak kaydedildi')
    #                 f.write('\n')
    #                 f.write(str(os.path.join(imageSaveLocation, image_name)) + ' olarak kaydedildi')
    #                 f.write('\n')
    #                 f.close()
    return image