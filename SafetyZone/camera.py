import os
from cv2 import cv2
import numpy as np
from django.conf import settings
from SafetyZone import object_detector
# from SafetyZone.object_detection import object_detection_folder_onnxTF2
from .isIn import check_rois
from .draw_poly import draw_poly, draw_poly_
import logging
from threading import Thread
import time

from django.shortcuts import render
from .models import *
from .log_functions import *
import cv2
import threading
from SafetyZone import rois 
# from .plc import Plc

from SafetyZone.models import Project, Config, ProjectConfig
# LOG
log_array = {"type": [],"content": []}
log_array["type"].append("debug")
log_array["content"].append(str("camera.py Kutuphaneleri Yuklendi"))
log_for_plc_bit_change(log_array)
####################

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
        # LOG
        log_array = {"type": [],"content": []}
        log_array["type"].append("debug")
        log_array["content"].append(str(f"Kamera Goruntusu Islenmeye Baslandi"))
        log_for_plc_bit_change(log_array)
        ####################
        try:
            self.video = cv2.VideoCapture(0)
        except:
            # LOG
            log_array = {"type": [],"content": []}
            log_array["type"].append("error")
            log_array["content"].append(str(f"Kamera Baglantisi Saglanamadi"))
            log_for_plc_bit_change(log_array)
            print(f"Kamera Baglantisi Saglanamadi")
            ####################
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=(), daemon=True).start()
        self.detect = object_detector.ObjectDetection()
        # self.detect.setDaemon(True)

    def __del__(self):
        self.video.release()

    def get_frame(self, method):
        image = self.frame
        # LOG
        log_array = {"type": [],"content": []}
        log_array["type"].append("debug")
        log_array["content"].append(str(f"Kameradaki Frame Alindi."))
        log_for_plc_bit_change(log_array)
        ####################
        orj_image = image.copy()
        _, jpeg = cv2.imencode('.jpg', image)
        image_detected, isIn, boxes, scores, classes = self.detect.object_detection(image)
        # LOG
        log_array = {"type": [],"content": []}
        log_array["type"].append("debug")
        log_array["content"].append(str(f"Frame, Goruntu Islemeden Dondu."))
        log_for_plc_bit_change(log_array)
        ####################
        image_detected = draw_polly_and_check_isin(image_detected, boxes, scores, classes, isIn , method)
        # LOG
        log_array = {"type": [],"content": []}
        log_array["type"].append("debug")
        log_array["content"].append(str(f"Frame, Polly cizimi ve Icindemi Kontrolunden Dondu"))
        log_for_plc_bit_change(log_array)
        ####################
        _, image = cv2.imencode('.jpg', image_detected)
        # # LOG
        # log_for_processed_image(orj_image, image_detected)
        # #############
        return jpeg.tobytes(), image.tobytes()

    def update(self):
        while True:
            try:
                (self.grabbed, self.frame) = self.video.read()
            except:
                # LOG
                log_array = {"type": [],"content": []}
                log_array["type"].append("error")
                log_array["content"].append(str(f"Kameradan Goruntu cekilemedi"))
                log_for_plc_bit_change(log_array)
                print(f"Kameradan Goruntu cekilemedi")
                ####################

def gen(camera):
    # LOG
    log_array = {"type": [],"content": []}
    log_array["type"].append("debug")
    log_array["content"].append(str(f"Orjinal Goruntu Arayuzde Goruntulenmek Icin Isleme Basladi"))
    log_for_plc_bit_change(log_array)
    ####################
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
    # LOG
    log_array = {"type": [],"content": []}
    log_array["type"].append("debug")
    log_array["content"].append(str(f"Detection Edilen Goruntu Arayuzde Goruntulenmek Icin Isleme Basladi"))
    log_for_plc_bit_change(log_array)
    ####################
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
    # LOG
    log_array = {"type": [],"content": []}
    log_array["type"].append("debug")
    log_array["content"].append(str(f"Polly Cizimi Tamamlandi"))
    log_for_plc_bit_change(log_array)
    ####################
    for i in range(min(12, boxes.shape[0])):
        if scores is None or scores[i] > 0.7:
            box = tuple(boxes[i].tolist())
            for index, polly_point in enumerate(poly_point_list):
                if int(classes[i]) == int(class_id[index]):
                    isIn = check_rois(image, polly_point, box, "middlecenter")
                    # LOG
                    log_array = {"type": [],"content": []}
                    log_array["type"].append("debug")
                    log_array["content"].append(str(f"Tespit Edilen Nesneler Icindemi Kontrol Edildi"))
                    log_for_plc_bit_change(log_array)
                    ####################
                    if isIn == True:
                        draw_isIn = isIn
                    image = draw_poly(image, polly_point, draw_isIn)
                    # LOG
                    log_array = {"type": [],"content": []}
                    log_array["type"].append("debug")
                    log_array["content"].append(str(f"Tespit Edilen Nesneler'in Konumuna Gore Polly Rengi Degistirildi"))
                    log_for_plc_bit_change(log_array)
                    ####################


            # isIn = check_rois(image, poly_point_list[0], box, RoiAlign[0]['configValue'])

    # print(isIn)
    # if isIn != PLC2.bit_value:
    #     if method == "DETECTION":
    #        LOG
    #        log_array = {"type": [],"content": []}
    #        log_array["type"].append("debug")
    #        log_array["content"].append(str("Sonuc degisti -**- "))
    #        log_array["type"].append("debug")
    #        log_array["content"].append(str("PLC'den okunan deger: " + str(PLC2.bit_value)))
    #        log_array["type"].append("debug")
    #        log_array["content"].append(str("Detection sonucu : " + str(isIn))))
    #        log_for_plc_bit_change(log_array)
    #        ####################
    #         if isIn!= None:
    #             PLC3.Set_bit(DB=90, DBX=4, DB_X=1, value=isIn)
    #         else:
    #             pass
    return image

