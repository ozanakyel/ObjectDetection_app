import threading
import cv2
import time
# import numpy as np
# import os


from SafetyZone.models import Project, Config, ProjectConfig
# from SafetyZone import rois 
# from django.conf import settings
from SafetyZone import object_detector
from .server_utils import draw_polly_and_check_isin
# from .plc import Plc




# configs = ProjectConfig.objects.filter(projectID_id = 1).values()
# imageSaveLocation = configs[49]['configValue']
# serverLogLocation = configs[45]['configValue']

# PLC = Plc('10.15.221.254', PlcRack=0, PlcSlot=1)
# PLC2 = Plc('10.15.221.254', PlcRack=0, PlcSlot=1)
# PLC3 = Plc('10.15.221.254', PlcRack=0, PlcSlot=1)

# threading.Thread(target=PLC.Read_Bit, args=(90, 4, 0, 0.0275), daemon=True).start()
# threading.Thread(target=PLC2.Read_Bit, args=(90, 4, 1, 0.0275), daemon=True).start()


# os.chdir(os.path.join(os.getcwd(),'SafetyZone'))
# ROIS_PATH = os.path.join(os.getcwd(),'rois.json')

#to capture video class
# MODEL_NAME = 'Mask-Rcnn'
MODEL_NAME = 'Fast-Rcnn'

class VideoCamera(object):
    def __init__(self):
        # self.video = cv2.VideoCapture('rtsp://admin:Abc1234*@10.16.222.253/')
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        self.jpeg = None
        self.image = None
        self.detect = object_detector.ObjectDetection()
        # self.detect.setDaemon(True)
        self.start_time = time.time()
        self.display_time = 1
        self.fc = 0
        self.FPS = 0
        print("başladı")
        # threading.Thread(target=self.update, args=(), daemon=True).start()
        threading.Thread(target=self.get_frame, args=(), daemon=True).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
            image = self.frame
            self.fc+=1
            TIME = time.time() - self.start_time
            
            if (TIME) >= self.display_time :
                self.FPS = self.fc / (TIME)
                self.fc = 0
                self.start_time = time.time()

            fps_disp = "FPS: "+str(self.FPS)[:5]
            
            # Add FPS count on frame
            # WEB_SOCKET.send(fps_disp)
            image = cv2.putText(image, fps_disp, (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            _, jpeg = cv2.imencode('.jpg', image)
            image_detected, boxes, scores, classes = self.detect.object_detection(image, MODEL_NAME)
            image_detected = draw_polly_and_check_isin(image_detected, boxes, scores, classes)

            _, image = cv2.imencode('.jpg', image_detected)
            self.jpeg = jpeg.tobytes()
            self.image = image.tobytes()

    # def update(self):
    #     print("******UPDATE**********")
    #     while True:
    #         (self.grabbed, self.frame) = self.video.read()

    def gen(self):
        print("******GEN**********")
        while True:     
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + self.jpeg + b'\r\n\r\n')

    def gen2(self):
        while True:
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + self.image + b'\r\n\r\n')

##################################
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