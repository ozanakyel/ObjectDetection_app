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
        point = (x_max-((x_max-x_min)/2), (y_max-(y_max-y_min)/2))

    pointX = Point(point)
    polygon = Polygon(polygon)

    result = (polygon.contains(pointX))
    # print(result)
    # if result == None:
    #     result = False
    return result
