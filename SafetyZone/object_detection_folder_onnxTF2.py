import onnxruntime as rt
import numpy as np
from PIL import Image, ImageDraw, ImageColor, ImageFont
import math
import matplotlib.pyplot as plt
import os
from utils import visualization_utils as vis_util
import cv2

# params
#MODEL = "C:/tf1/models/research/object_detection/tensorflow-onnx-master/model.onnx"
MODEL = "C:/tensorflow1/models/research/object_detection/object-detection-w_onnx/modelAHMET.onnx"
#MODEL = "ssd_mobilenet_v1_coco_2018_01_28/model.onnx"
PROTOTXT = 'label.prototxt'
IMAGE = 'images/train_aug_1551.jpg'
IMAGE_FOLDER = r'C:\tensorflow1\models\research\object_detection\object-detection-w_onnx\imagesAhmet'

# force tf2onnx to cpu
os.environ['CUDA_VISIBLE_DEVICES'] = "-1"

# inference session

sess = rt.InferenceSession(MODEL)
outputs = ['detection_anchor_indices', 'detection_boxes', 'detection_classes', 'detection_multiclass_scores', 'detection_scores', 'num_detections', 'raw_detection_boxes', 'raw_detection_scores']
#outputs = ["detection_boxes:0", "detection_classes:0", "detection_scores:0", "num_detections:0"]

icerik = os.listdir(IMAGE_FOLDER)

for i in icerik:
    IMAGE = os.path.join(IMAGE_FOLDER, i)
    img = Image.open(IMAGE)
    img_data = np.array(img.getdata()).reshape(img.size[1], img.size[0], 3)
    img_data = np.expand_dims(img_data.astype(np.uint8), axis=0)

    result = sess.run(outputs, {"input_tensor": img_data})
    print(len(result))
    #detection_boxes, detection_classes, detection_scores, num_detections= result
    detection_anchor_indices, detection_boxes, detection_classes, detection_multiclass_scores, detection_scores, num_detections, raw_detection_boxes, raw_detection_scores = result
    

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

    coco_classes = []

    with open(PROTOTXT) as lines:
        for line in lines:
            coco_classes.append(line.strip())

    font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial.ttf", 22)


    batch_size = num_detections.shape[0]
    draw = ImageDraw.Draw(img)
    for batch in range(0, batch_size):

        for detection in range(0, int(num_detections[batch])):
            score_thresh = detection_scores[batch][detection]
            if score_thresh >= 0.1:
                print(score_thresh)
                c = detection_classes[batch][detection]
                d = detection_boxes[batch][detection]
                draw_detection(draw, d, c)

    #print(detection_scores)
    plt.figure(figsize=(8, 8))
    plt.axis('off')
    pathIM = 'C:/tensorflow1/models/research/object_detection/object-detection-w_onnx/imagesAhmet/sonuc'
    #plt.savefig()
    image = np.array(img)
    image2 = image[:, :, ::-1].copy()
    cv2.imshow("GORUNTU",image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #plt.show()
