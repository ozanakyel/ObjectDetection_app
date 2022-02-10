import os
from cv2 import cv2
import numpy as np
import tensorflow as tf
import sys
import time

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from numpy import asarray

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")

# Import utilites
from SafetyZone.object_detection.utils import label_map_util
from SafetyZone.object_detection.utils import visualization_utils as vis_util

from tensorflow import ConfigProto
from tensorflow import InteractiveSession

class ObjectDetection(object):
    def __init__(self):
        print("**********************************")
        self.config = ConfigProto()
        self.config.gpu_options.allow_growth = True
        self.config.gpu_options.per_process_gpu_memory_fraction = 0.8
        self.session = InteractiveSession(config=self.config)

        # Name of the directory containing the object detection module we're using
        self.MODEL_NAME = 'faster_rcnn_inception_v2_coco_2018_01_28'
        # select image folder
        # Grab path to current working directory
        self.CWD_PATH = os.getcwd()
        # Number of classes the object detector can identify
        self.NUM_CLASSES = 5

        # Path to frozen detection graph .pb file, which contains the model that is used
        # for object detection.
        self.PATH_TO_CKPT = os.path.join(self.CWD_PATH, 'SafetyZone\object_detection', self.MODEL_NAME, 'frozen_inference_graph.pb')

        # Path to label map file
        self.PATH_TO_LABELS = os.path.join(self.CWD_PATH,'SafetyZone\object_detection\data','mscoco_label_map.pbtxt')

        # Path to image
        # PATH_TO_IMAGE = os.path.join(r'C:\Users\ozan.akyel\Desktop\project 2021\siperlik toka\v4\valid',IMAGE_NAME) ################################# geri alman gerekebilir


        # Load the label map.
        # Label maps map indices to category names, so that when our convolution
        # network predicts `5`, we know that this corresponds to `king`.
        # Here we use internal utility functions, but anything that returns a
        # dictionary mapping integers to appropriate string labels would be fine
        self.label_map = label_map_util.load_labelmap(self.PATH_TO_LABELS)
        self.categories = label_map_util.convert_label_map_to_categories(self.label_map, max_num_classes=self.NUM_CLASSES, use_display_name=True)
        self.category_index = label_map_util.create_category_index(self.categories)

        # Load the Tensorflow model into memory.
        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            self.od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.PATH_TO_CKPT, 'rb') as fid:
                self.serialized_graph = fid.read()
                self.od_graph_def.ParseFromString(self.serialized_graph)
                tf.import_graph_def(self.od_graph_def, name='')

            self.sess = tf.Session(graph=self.detection_graph)

        # Define input and output tensors (i.e. data) for the object detection classifier

        # Input tensor is the image
        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')

        # Output tensors are the detection boxes, scores, and classes
        # Each box represents a part of the image where a particular object was detected
        self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')

        # Each score represents level of confidence for each of the objects.
        # The score is shown on the result image, together with the class label.
        self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')

        # Number of objects detected
        self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')

    def object_detection(self, image):

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_expanded = np.expand_dims(image_rgb, axis=0)

        # Perform the actual detection by running the model with the image as input
        # print('####################################')
        (boxes, scores, classes, num) = self.sess.run(
            [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
            feed_dict={self.image_tensor: image_expanded})

        # Draw the results of the detection (aka 'visulaize the results')

        vis_util.visualize_boxes_and_labels_on_image_array(
            image,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            self.category_index,
            use_normalized_coordinates=True,
            line_thickness=2,
            min_score_thresh=0.7,
            max_boxes_to_draw=12)

        pts = np.array([[1900, 1079], [1900, 70], 
                [150, 70], [150, 1079]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        isClosed = True
        # Blue color in BGR
        color = (255, 0, 0)
        # Line thickness of 2 px
        thickness = 2
        image = cv2.polylines(image, [pts], isClosed, color, thickness)

        a = np.squeeze(boxes)
        b = np.squeeze(scores)
        c = np.squeeze(classes).astype(np.int32)
        x = image.shape[0]
        y = image.shape[1]
        d1 = ImageDraw.Draw(Image.fromarray(image))
        for i in range(min(12, a.shape[0])):
            if b is None or b[i] > 0.7:
                box = tuple(a[i].tolist())
                # print('-------Class-------')
                # print(c[i])
                # print('-------Box-------')
                # print(box)
                startpoint = (int(y*box[1]), int(x*box[0]))
                endpoint = (int(y*box[3]), int(x*box[2]))
                if ( startpoint[0] < 1900 and startpoint[0] > 150 and endpoint[0] < 1900 and endpoint[0] > 150 and startpoint[1] < 1081 and startpoint[1] > 70 and endpoint[1] < 1081 and endpoint[1] > 70):
                    print("icinde")
                    # d1.text((0, 0), "NOK", fill =(255, 0, 0))
                else:
                    print("icinde degil")
                    # d1.text((0, 0), "OK", fill =(255, 0, 0))

        return image
