import os
from cv2 import cv2
import numpy as np
import tensorflow as tf
import sys
from numpy import asarray, isin
# from .log_functions import log_for_plc_bit_change


# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")

# Import utilites
from SafetyZone.object_detection.utils import label_map_util
from SafetyZone.object_detection.utils import visualization_utils as vis_util
from object_detection.utils import ops as utils_ops

from tensorflow import ConfigProto
from tensorflow import InteractiveSession

# MODEL_NAME = 'mask_rcnn_inception_v2_coco_2018_01_28'
# MODEL_NAME = 'faster_rcnn_inception_v2_coco_2018_01_28'
MODEL_NAME = 'ssd_inception_v2_coco_2018_01_28' 
LABEL_MAP = 'mscoco_label_map.pbtxt'
NUM_CLASSES = 5

class ObjectDetection(object):
    def __init__(self):
        self.config = ConfigProto()
        self.config.gpu_options.allow_growth = True
        self.config.gpu_options.per_process_gpu_memory_fraction = 0.8
        self.session = InteractiveSession(config=self.config)

        self.CWD_PATH = os.getcwd()

        self.PATH_TO_CKPT = os.path.join(self.CWD_PATH, 'SafetyZone\object_detection', MODEL_NAME, 'frozen_inference_graph.pb')


        # Path to label map file
        self.PATH_TO_LABELS = os.path.join(self.CWD_PATH,'SafetyZone\object_detection\data',LABEL_MAP)

        # Load the label map.
        self.label_map = label_map_util.load_labelmap(self.PATH_TO_LABELS)
        self.categories = label_map_util.convert_label_map_to_categories(self.label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
        self.category_index = label_map_util.create_category_index(self.categories)

        # # Load the Tensorflow model into memory.
        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            self.od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.PATH_TO_CKPT, 'rb') as fid:
                self.serialized_graph = fid.read()
                self.od_graph_def.ParseFromString(self.serialized_graph)
                tf.import_graph_def(self.od_graph_def, name='')

            self.sess = tf.Session(graph=self.detection_graph)

        # # Define input and output tensors (i.e. data) for the object detection classifier

        # # Input tensor is the image
        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')

        # # Output tensors are the detection boxes, scores, and classes
        # # Each box represents a part of the image where a particular object was detected
        self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')

        # # Each score represents level of confidence for each of the objects.
        # # The score is shown on the result image, together with the class label.
        self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')

        # # Number of objects detected
        self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')


    def run_inference_for_single_image(image, graph):
        with graph.as_default():
            with tf.Session() as sess:
            # Get handles to input and output tensors
                ops = tf.get_default_graph().get_operations()
                all_tensor_names = {output.name for op in ops for output in op.outputs}
                tensor_dict = {}
                for key in [
                    'num_detections', 'detection_boxes', 'detection_scores',
                    'detection_classes', 'detection_masks'
                ]:
                    tensor_name = key + ':0'
                    if tensor_name in all_tensor_names:
                        tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(
                            tensor_name)
                if 'detection_masks' in tensor_dict:
                    # The following processing is only for single image
                    detection_boxes = tf.squeeze(tensor_dict['detection_boxes'], [0])
                    detection_masks = tf.squeeze(tensor_dict['detection_masks'], [0])
                    # Reframe is required to translate mask from box coordinates to image coordinates and fit the image size.
                    real_num_detection = tf.cast(tensor_dict['num_detections'][0], tf.int32)
                    detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
                    detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
                    detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
                        detection_masks, detection_boxes, image.shape[0], image.shape[1])
                    detection_masks_reframed = tf.cast(
                        tf.greater(detection_masks_reframed, 0.5), tf.uint8)
                    # Follow the convention by adding back the batch dimension
                    tensor_dict['detection_masks'] = tf.expand_dims(
                        detection_masks_reframed, 0)
                image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

                # Run inference
                output_dict = sess.run(tensor_dict,
                                        feed_dict={image_tensor: np.expand_dims(image, 0)})

                # all outputs are float32 numpy arrays, so convert types as appropriate
                output_dict['num_detections'] = int(output_dict['num_detections'][0])
                output_dict['detection_classes'] = output_dict[
                    'detection_classes'][0].astype(np.uint8)
                output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
                output_dict['detection_scores'] = output_dict['detection_scores'][0]
                if 'detection_masks' in output_dict:
                    output_dict['detection_masks'] = output_dict['detection_masks'][0]
        return output_dict
    def object_detection(self, image, model_name):
        if model_name == 'Fast-Rcnn':
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image_expanded = np.expand_dims(image_rgb, axis=0)

            # Perform the actual detection by running the model with the image as input
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
                max_boxes_to_draw=3)

            return image, boxes, scores, classes
        elif model_name == 'Mask-Rcnn':
            category_index = label_map_util.create_category_index_from_labelmap(self.PATH_TO_LABELS, use_display_name=True)

            def run_inference_for_single_image(image, graph):
                with graph.as_default():
                    with tf.Session() as sess:
                        # Get handles to input and output tensors
                        ops = tf.get_default_graph().get_operations()
                        all_tensor_names = {output.name for op in ops for output in op.outputs}
                        tensor_dict = {}
                        for key in [
                            'num_detections', 'detection_boxes', 'detection_scores',
                            'detection_classes', 'detection_masks'
                        ]:
                            tensor_name = key + ':0'
                            if tensor_name in all_tensor_names:
                                tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(
                                    tensor_name)
                        if 'detection_masks' in tensor_dict:
                            # The following processing is only for single image
                            detection_boxes = tf.squeeze(tensor_dict['detection_boxes'], [0])
                            detection_masks = tf.squeeze(tensor_dict['detection_masks'], [0])
                            # Reframe is required to translate mask from box coordinates to image coordinates and fit the image size.
                            real_num_detection = tf.cast(tensor_dict['num_detections'][0], tf.int32)
                            detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
                            detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
                            detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
                                detection_masks, detection_boxes, image.shape[0], image.shape[1])
                            detection_masks_reframed = tf.cast(
                                tf.greater(detection_masks_reframed, 0.5), tf.uint8)
                            # Follow the convention by adding back the batch dimension
                            tensor_dict['detection_masks'] = tf.expand_dims(
                                detection_masks_reframed, 0)
                        image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

                        # Run inference
                        output_dict = sess.run(tensor_dict,
                                                feed_dict={image_tensor: np.expand_dims(image, 0)})

                        # all outputs are float32 numpy arrays, so convert types as appropriate
                        output_dict['num_detections'] = int(output_dict['num_detections'][0])
                        output_dict['detection_classes'] = output_dict[
                            'detection_classes'][0].astype(np.uint8)
                        output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
                        output_dict['detection_scores'] = output_dict['detection_scores'][0]
                        if 'detection_masks' in output_dict:
                            output_dict['detection_masks'] = output_dict['detection_masks'][0]
                return output_dict
            
            # image_np = load_image_into_numpy_array(image)
            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # Actual detection.
            output_dict = run_inference_for_single_image(image, self.detection_graph)
            # Visualization of the results of a detection.
            vis_util.visualize_boxes_and_labels_on_image_array(
                image,
                output_dict['detection_boxes'],
                output_dict['detection_classes'],
                output_dict['detection_scores'],
                category_index,
                instance_masks=output_dict.get('detection_masks'),
                use_normalized_coordinates=True,
                max_boxes_to_draw = 1,
                line_thickness=1
                )
            return image, output_dict['detection_boxes'], output_dict['detection_scores'], output_dict['detection_classes']
