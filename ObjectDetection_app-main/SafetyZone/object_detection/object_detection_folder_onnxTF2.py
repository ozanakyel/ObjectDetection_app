import onnxruntime as rt
import numpy as np
from PIL import Image, ImageDraw, ImageColor, ImageFont
import math
import matplotlib.pyplot as plt
import os
from utils import visualization_utils as vis_util
from cv2 import cv2
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon



# params
#MODEL = "C:/tf1/models/research/object_detection/tensorflow-onnx-master/model.onnx"
MODEL = "C:/Users/Harun/Desktop/ObjectDetection_app/SafetyZone/object_detection/model.onnx"
#MODEL = "ssd_mobilenet_v1_coco_2018_01_28/model.onnx"
PROTOTXT = 'label.prototxt'

THRESH_HOLD = 0.7
# IMAGE = 'images/train_aug_1551.jpg'
IMAGE_FOLDER = r'C:/Users/Harun/Desktop/ObjectDetection_app/SafetyZone/object_detection/images'

# force tf2onnx to cpu
os.environ['CUDA_VISIBLE_DEVICES'] = "-1"

# inference session

sess = rt.InferenceSession(MODEL)
outputs = ['detection_anchor_indices', 'detection_boxes', 'detection_classes', 'detection_multiclass_scores', 'detection_scores', 'num_detections', 'raw_detection_boxes', 'raw_detection_scores']
#outputs = ["detection_boxes:0", "detection_classes:0", "detection_scores:0", "num_detections:0"]

icerik = os.listdir(IMAGE_FOLDER)


    

    # draw results
def draw_detection(draw, d, c):
    width, height = draw.im.size
    # the box is relative to the image size so we multiply with height and width to get pixels.
    top = d[0] * height
    left = d[1] * width
    bottom = d[2] * height
    right = d[3] * width
    top = max(0, np.floor(top + 0.5).astype('int32'))
    left = max(0, np.floor(left + 0.5).astype('int32'))
    bottom = min(height, np.floor(bottom + 0.5).astype('int32'))
    right = min(width, np.floor(right + 0.5).astype('int32'))
    label = coco_classes[c.astype('int32') - 1] # shift to zero element
    label_size = draw.textsize(label)
    text_origin = tuple(np.array([left + 1, top + 1]))
    color = ImageColor.getrgb("yellow")
    thickness = 0
    draw.rectangle([left + thickness, top + thickness, right - thickness, bottom - thickness], outline=color)
    draw.text(text_origin, label, fill=color, font=font)
print('geldi2')

coco_classes = []

with open(PROTOTXT) as lines:
    for line in lines:
        coco_classes.append(line.strip())

font = ImageFont.truetype("C://Windows//Fonts//Arial.ttf", 22)

def onnx2_object_detection(image, model):

    color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img= Image.fromarray(color_coverted)
    sess = rt.InferenceSession(model)
    outputs = ['detection_anchor_indices', 'detection_boxes', 'detection_classes', 'detection_multiclass_scores',
               'detection_scores', 'num_detections', 'raw_detection_boxes', 'raw_detection_scores']
    img_data = np.array(img.getdata()).reshape(img.size[1], img.size[0], 3)
    img_data = np.expand_dims(img_data.astype(np.uint8), axis=0)

    result = sess.run(outputs, {"input_tensor": img_data})
    #detection_boxes, detection_classes, detection_scores, num_detections= result
    detection_anchor_indices, detection_boxes, detection_classes, detection_multiclass_scores, detection_scores, num_detections, raw_detection_boxes, raw_detection_scores = result

    return detection_classes, detection_boxes, detection_scores, num_detections

def find_boxes(detection_classes, detection_boxes, detection_scores, num_detections):
    batch_size = num_detections.shape[0]
    res_classes = []
    res_boxes = []
    res_scores = []
    for batch in range(0, batch_size):

        for detection in range(0, int(num_detections[batch])):
            score_thresh = detection_scores[batch][detection]
            if score_thresh >= THRESH_HOLD:
                res_classes.append(detection_classes[batch][detection])
                res_boxes.append(detection_boxes[batch][detection])
                res_scores.append(score_thresh)
    # eğer NMS gerekirse https://bitbucket.org/tomhoag/opencv-text-detection/src/master/opencv_text_detection/text_detection.py   nms kütüphanesi ile işlem yapıyor

    print(f" example1 === res_boxes : {res_boxes} '/n' res_classes : {res_classes} '/n' res_scores : {res_classes}")
    # res_boxes : [array([0.4223325 , 0.7818462 , 0.87800217, 0.88146704], dtype=float32), array([0.4025001 , 0.05265692, 0.86825746, 0.16901194], dtype=float32), array([0.39042836, 0.18137299, 0.81469727, 0.29084346], dtype=float32), array([0.3722965 , 0.52270657, 0.8079053 , 0.6144761 ], dtype=float32), array([0.41471854, 0.40537292, 0.92972225, 0.5313649 ], dtype=float32), array([0.41969037, 0.34717906, 0.92240906, 0.43294248], dtype=float32), array([0.39640924, 0.6357784 , 0.8778954 , 0.778055  ], dtype=float32), array([0.17301251, 0.7340291 , 0.41380104, 0.80958426], dtype=float32), array([0.41938147, 0.32814094, 0.9256315 , 0.60606474], dtype=float32)] '
    # res_classes : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # res_scores : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    return res_boxes, res_classes, res_scores

def drawed_image(image, boxes, classes, scores):
    for i in range(0, len(scores)):
        print(boxes[0])
        width = image.shape[0]
        height = image.shape[1]
        x_min = int(boxes[i][0]*width)
        y_min = int(boxes[i][1]*height)
        x_max = int(boxes[i][2]*width)
        y_max = int(boxes[i][3]*height)
        cv2.putText(image, (coco_classes[int(classes[i])-1]+ ' ' + str(round(scores[i]*100, 2))), (y_min, x_min), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.rectangle(image, (y_min, x_min), (y_max, x_max), (255, 255, 255), 2)
        print(f"example2 === boxes : {boxes[i]} '/n' classes : {classes[i]} /n scores : {scores[i]}")
        # example
        # boxes : [0.41938147 0.32814094 0.9256315  0.60606474]
        # classes : 1.0
        # scores : 0.26112356781959534
    return image

def check_rois(image, box, rois, position):
    width = image.shape[0]
    height = image.shape[1]
    x_min = int(box[0] * width)
    y_min = int(box[1] * height)
    x_max = int(box[2] * width)
    y_max = int(box[3] * height)
    if position == 'bottomcenter':
        point = (x_max-(x_max-x_min/2), y_max)
    if position == 'middlecenter':
        point = (x_max-((x_max-x_min)/2), y_max-(y_max-y_min)/2)

    pointX = Point(point)
    polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
    result = (polygon.contains(pointX))
    return result

def check_id(classes, id):
    if i in classes:
        result = True
    else:
        result = False
    return result

for i in icerik:
    IMAGE = os.path.join(IMAGE_FOLDER, i)
    img = cv2.imread(IMAGE)

    detection_classes, detection_boxes, detection_scores, num_detections = onnx2_object_detection(img, MODEL)
    # detection_classes : [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.   .......     1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]] '
    # ' detection_boxes : [[[0.4223325  0.7818462  0.87800217 0.88146704] ............  [0.         0.         0.         0.        ]]] '
    # detection_scores : [[9.9997866e-01 9.9997568e-01 9.9996364e-01 9.9995685e-01 9.9994755e-01 ........ 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00]] '
    # num_detection : [100.]
    print(f" example3 === detection_classes : {detection_classes} '/n' detection_boxes : {detection_boxes} '/n' detection_scores : {detection_scores} '/n' num_detection : {num_detections}")

    boxes, classes, scores = find_boxes(detection_classes, detection_boxes, detection_scores, num_detections)
    # boxes : [array([0.4223325 , 0.7818462 , 0.87800217, 0.88146704], dtype=float32), array([0.4025001 , 0.05265692, 0.86825746, 0.16901194], dtype=float32), array([0.39042836, 0.18137299, 0.81469727, 0.29084346], dtype=float32), array([0.3722965 , 0.52270657, 0.8079053 , 0.6144761 ], dtype=float32), array([0.41471854, 0.40537292, 0.92972225, 0.5313649 ], dtype=float32), array([0.41969037, 0.34717906, 0.92240906, 0.43294248], dtype=float32), array([0.39640924, 0.6357784 , 0.8778954 , 0.778055  ], dtype=float32), array([0.17301251, 0.7340291 , 0.41380104, 0.80958426], dtype=float32), array([0.41938147, 0.32814094, 0.9256315 , 0.60606474], dtype=float32)] '
    # classes : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] '
    # scores : [0.99997866, 0.9999757, 0.99996364, 0.99995685, 0.99994755, 0.9999292, 0.99991715, 0.9951521, 0.26112357]
    print(f"example4 ==== boxes : {boxes} '/n' classes : {classes} '/n' scores : {scores}")


    image = drawed_image(img, boxes, classes, scores)

    cv2.imshow("GORUNTU",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # print(f"boxes : {boxes} '/n' classes : {classes} '/n' scores : {scores}")
    # draw = ImageDraw.Draw(img)




    """for batch in range(0, batch_size):

        for detection in range(0, int(num_detections[batch])):
            score_thresh = detection_scores[batch][detection]
            if score_thresh >= 0.1:
                print(score_thresh)
                c = detection_classes[batch][detection]
                d = detection_boxes[batch][detection]

                print(f"scores : {score_thresh} '/n' boxes : {d} '/n' classes : {c}")"""

    #print(detection_scores)
    plt.figure(figsize=(8, 8))
    plt.axis('off')
    pathIM = 'C:/tensorflow1/models/research/object_detection/object-detection-w_onnx/imagesAhmet/sonuc'
    #plt.savefig()
    image = np.array(img)
    image2 = image[:, :, ::-1].copy()
    # cv2.imshow("GORUNTU",image2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #plt.show()
