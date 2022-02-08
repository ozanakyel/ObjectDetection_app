import os,urllib.request
from cv2 import cv2
import numpy as np
from django.conf import settings
# from polls import object_detector
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

#to capture video class
class VideoCamera(object):
    def __init__(self):
        # self.video = cv2.VideoCapture('http://192.168.1.38:8081/video')
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
        # self.detect = object_detector.ObjectDetection()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        # image_detected = self.detect.object_detection(image)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

