import numpy as np
from cv2 import cv2

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