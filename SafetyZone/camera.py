import os,urllib.request
from cv2 import cv2
import numpy as np
from django.conf import settings
from SafetyZone import object_detector
import logging
from threading import Thread
import time

from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from PIL import Image
import datetime

from SafetyZone.models import Project, Config, ProjectConfig

configs = ProjectConfig.objects.filter(projectID_id = 1).values()
imageSaveLocation = configs[49]['configValue']
serverLogLocation = configs[45]['configValue']


#to capture video class
class VideoCamera(object):
    def __init__(self):
        # self.video = cv2.VideoCapture('http://192.168.1.38:8081/video')
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
        self.detect = object_detector.ObjectDetection()
        self.i = 0

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        image_orj = image.copy()
        _, jpeg = cv2.imencode('.jpg', image)
        image_detected, isIn = self.detect.object_detection(image)
        _, image = cv2.imencode('.jpg', image_detected)
        if (isIn == True):
            image_name = str(self.i) + '_detected' +'.jpg'
            image_name_orj = str(self.i) +'.jpg'
            self.i += 1
            # cv2.imwrite(os.path.join(imageSaveLocation, image_name_orj), image_orj)
            # cv2.imwrite(os.path.join(imageSaveLocation, image_name), image_detected)
            # print(os.path.join(configs[50]['configValue'], image_name), 'olarak kaydedildi')
            path = str(datetime.date.today()) + '.txt'
            direction =  os.path.join(str(serverLogLocation), path)
            if not os.path.exists(direction):
                with open( direction , 'w+') as f:
                    f.write(str(os.path.join(imageSaveLocation, image_name_orj)) + ' olarak kaydedildi')
                    f.write('\n')
                    f.write(str(os.path.join(imageSaveLocation, image_name)) + ' olarak kaydedildi')
                    f.write('\n')
                    f.close()
            else:
                with open( direction , 'a') as f:
                    f.write(str(os.path.join(imageSaveLocation, image_name_orj)) + ' olarak kaydedildi')
                    f.write('\n')
                    f.write(str(os.path.join(imageSaveLocation, image_name)) + ' olarak kaydedildi')
                    f.write('\n')
                    f.close()
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

# def boxes(box):
#     while True:
#         boxes,clases = box.get_boxes()
#         print('-------Class-------')
#         print(clases)
#         print('-------Box-------')
#         print(boxes)
