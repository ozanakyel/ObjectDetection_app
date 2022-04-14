import matplotlib.pyplot as plt
import json
import websocket 
import numpy as np
import time
import threading
# import snap7.util

from cv2 import cv2
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
# from SafetyZone.server_utils import WebSocket, get_rois, show_ok_nok, draw_poly_


WEBSOCKET_URL = "ws://127.0.0.1:8081/ws/socket-server/"
class WebSocket(object):
    def __init__(self):
        self.ws = websocket.create_connection(WEBSOCKET_URL)
    
    def send(self, message):
        self.ws.send(message)

WEB_SOCKET = WebSocket()
ROIS_PATH = r'C:\Users\Harun\Desktop\ObjectDetection_app\ObjectDetection_app-main\SafetyZone\rois.json'



def get_rois(file_path):

    with open(file_path, 'r') as j:
        Lines = j.readlines()

    sayac = 0
    res = []
    ClassId = []
    PolyPointList = []
    IsObjectHave = []
    Reverse = []
    for index, line in enumerate(Lines):
        sayac+=1
        if not (sayac == len(Lines) or sayac == 1):
            json_acceptable_string = str(line).replace("'", "\"")

            if json_acceptable_string[-2] == ",":
                json_acceptable_string = json_acceptable_string[: -2]
            ClassId.append(json.loads(json_acceptable_string)["ClassId"])
            IsObjectHave.append(json.loads(json_acceptable_string)["IsObjectHave"])
            Reverse.append(json.loads(json_acceptable_string)["Reverse"])
            res = []
            res.append(json.loads(json_acceptable_string)["PolyPointList"])
            point = []
            for i in res[0]:
                x = i["X"]
                y = i["Y"]
                point.append([x, y])
            PolyPointList.append(point)

    return ClassId, PolyPointList, IsObjectHave, Reverse

ROIS_CLASS_ID, ROIS_POLY_POINT_LIST, IS_OBJECT_HAVE, REVERSE = get_rois(ROIS_PATH)

def draw_polly_and_check_isin(image, boxes, scores, classes):

    # RoiAlign = ProjectConfig.objects.filter(configKeyID_id = 53).values()
    boxes = np.squeeze(boxes)
    scores = np.squeeze(scores)
    classes = np.squeeze(classes).astype(np.int32)
    x = image.shape[0]
    y = image.shape[1]
    # TODO Roi sayisina gore total result dondurulecek sekilde revize edilecek.
    draw_isIn = False
    for polly_point in ROIS_POLY_POINT_LIST:
        draw_poly_(image, polly_point)
    polly_is_in = []
    for i in range(min(12, boxes.shape[0])):
        if scores is None or scores[i] > 0.7:
            box = tuple(boxes[i].tolist())
            
            for index, polly_point in enumerate(ROIS_POLY_POINT_LIST):
                if int(classes[i]) == int(ROIS_CLASS_ID[index]):
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
    WEB_SOCKET.send(str(message))


            # isIn = check_rois(image, ROIS_POLY_POINT_LIST[0], box, RoiAlign[0]['configValue'])

    # print(isIn)
    # if isIn != PLC2.bit_value:
    #     if method == "DETECTION":
    #         if isIn!= None:
    #             PLC3.Set_bit(DB=90, DBX=4, DB_X=1, value=isIn)
    #         else:
    #             pass
    return image
def draw_poly(image, polygon, isIn):
    pts = np.array(polygon, np.int32)
    pts = pts.reshape((-1, 1, 2))
    if isIn == True:
        # Blue color in BGR
        color = (0, 0, 255)
        # Line thickness of 2 px
        thickness = 2
        image = cv2.polylines(image, [pts], True, color, thickness)
        # image = cv2.putText(image, 'NOK', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1, cv2.LINE_AA)
    else:
        color = (255, 0, 0)
        # Line thickness of 2 px
        thickness = 2
        image = cv2.polylines(image, [pts], True, color, thickness)
        # image = cv2.putText(image, 'OK', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
    return image
def show_ok_nok (image, isIn):
    if isIn == True:
        # Blue color in BGR
        image = cv2.putText(image, 'NOK', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
    else:
        image = cv2.putText(image, 'OK', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
    return image
def draw_poly_(image, polygon):
    pts = np.array(polygon, np.int32)
    pts = pts.reshape((-1, 1, 2))
    color = (255, 0, 0)
    thickness = 2
    image = cv2.polylines(image, [pts], True, color, thickness)
    return image
def check_rois(image, polygon, box, position):
    width = image.shape[0]
    height = image.shape[1]
    x_min = box[0] * width
    y_min = box[1] * height
    x_max = box[2] * width
    y_max = box[3] * height
    if position == 'BottomCenter':
        point = (x_max-((x_max-x_min)/2), y_max)
    if position == 'middlecenter':
        point = (x_max-((x_max-x_min)/2), (y_max-(y_max-y_min)/2))

    pointX = Point(point)
    polygon = Polygon(polygon)

    result = (polygon.contains(pointX))
    # print(result)
    # if result == None:
    #     result = False
    return result



"""import snap7

PlcIp = '10.15.221.254'
PlcRack = 0
PlcSlot = 0
PlcCpu = 30
IstasyonDB = 'DB90'
IstasyonDB = int(IstasyonDB[2:])
OperasyonBasladiDB = 'DBX0.0'
OperasyonTamamlandiDB = 'DBX0.1'

plc = snap7.client.Client()
plc.connect(PlcIp, PlcRack, PlcSlot)
reading = plc.db_read(90, 0, 2)
name = reading[0:256].decode('UTF-8').strip('\x00')
print(reading)"""

class Plc(object):
    def __init__(self, PlcIP, PlcRack, PlcSlot):
        self.bit_value = True
        self.client = snap7.client.Client()
        self.client.connect(PlcIP, PlcRack, PlcSlot)

    def Read_Byte(self, DB, DBX):
        buffer = self.client.db_read(DB, DBX, 1)
        # buffer -> type= byte array -> ascii -> string
        buffer_value = ord(buffer[0:256].decode('UTF-8'))  # only client.db_read(X, X, count) count =1
        return buffer_value , buffer     # string list

        # def write_byte(db_num, start_byte, byte_value):  # Byte yazma
        #     data = bytearray(1)
        #     snap7.util.set_byte(data, 0, byte_value)
        #     plc.db_write(db_num, start_byte, data)

    def Set_Byte(self, DB, DBX, value):
        try:
            data = bytearray(1)
            snap7.util.set_byte(data, 0, value)
            self.client.db_write(DB, DBX, data)
            result = True
        except:
            result = False
        return result


    def Read_Bit(self, DB, DBX, DB_X,pause):
        while True:
            buffer = self.client.db_read(DB, DBX, 1)
            byte_value = snap7.util.get_bool(buffer, 0, DB_X)
            self.bit_value = byte_value   # bool
            time.sleep(pause)


    def Set_bit(self, DB, DBX, DB_X, value):
        try:
            _,data = self.Read_Byte(DB,DBX)
            snap7.util.set_bool(data, 0, DB_X, value)
            self.client.db_write(DB, DBX, data)
            result = True
        except:
            result = False
        return result

