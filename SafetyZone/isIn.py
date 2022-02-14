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
