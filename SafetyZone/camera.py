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

#to capture video class
class VideoCamera(object):
    def __init__(self):
        # self.video = cv2.VideoCapture('http://192.168.1.38:8081/video')
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
        self.detect = object_detector.ObjectDetection()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        image_detected = self.detect.object_detection(image)
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

# def boxes(box):
#     while True:
#         boxes,clases = box.get_boxes()
#         print('-------Class-------')
#         print(clases)
#         print('-------Box-------')
#         print(boxes)
