import numpy as np
from PIL import Image, ImageDraw, ImageColor, ImageFont
import math
import matplotlib.pyplot as plt
import os

from cv2 import cv2
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

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
        point = (x_max-((x_max-x_min)/2), y_max-(y_max-y_min)/2)
        
    pointX = Point(point)
    polygon = Polygon(polygon)

    result = (polygon.contains(pointX))
    if result == True:
        image = cv2.putText(image, 'NOK', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
    else:
        image = cv2.putText(image, 'OK', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
    return result

# image = cv2.imread("settings.png")
# x = image.shape[0]
# y = image.shape[1]
# box = (0.1903514415025711, 0.007332114968448877, 0.9890193939208984, 0.747791588306427)
# polygon = [[1, 10], [450, 10], [435, 245], [1, 590]]

# pts = np.array(polygon, np.int32)
# pts = pts.reshape((-1,1,2))
# image = cv2.polylines(image, [pts], True, (255, 0, 0), 2)
# startpoint = (int(y*0.007332114968448877), int(x*0.1903514415025711))
# endpoint = (int(y*0.747791588306427), int(x*0.9890193939208984))
# cv2.rectangle(image, startpoint, endpoint, (0,255, 0), 3)
# cv2.imshow('image',image)
# cv2.waitKey(0)
# print(check_rois(image,polygon, box, "middlecenter"))

# import os
# import numpy as np
# import sys
# import time
# import cv2

# # Polygon corner points coordinates

# path = r'C:\Users\Harun\Desktop\settings.png'

# image = cv2.imread(path)
# print(image.shape)
# x = image.shape[0]
# y = image.shape[1]
# pts = np.array([[110, 70], [110, 160], 
                # [110, 800], [800, 800], 
                # [800, 70]],
            # np.int32)
        
# pts = pts.reshape((-1, 1, 2))
        
# isClosed = True
        
        # # Blue color in BGR
# color = (255, 0, 0)
# color2 = (255, 255, 0)
        
        # # Line thickness of 2 px
# thickness = 2
# image = cv2.polylines(image, [pts], isClosed, color, thickness)
# startpoint = (int(y*0.007332114968448877), int(x*0.1903514415025711))
# endpoint = (int(y*0.747791588306427), int(x*0.9890193939208984))
# cv2.rectangle(image, startpoint, endpoint, (0,255, 0), 3)
# cv2.imshow('image', image)
# cv2.waitKey(0)


# # (0.1903514415025711, 0.007332114968448877, 0.9890193939208984, 0.747791588306427)