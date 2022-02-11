import matplotlib.pyplot as plt
import json
import ast

def get_rois(file_path):

    with open(file_path, 'r') as j:
        Lines = j.readlines()

    sayac = 0
    res = []
    ClassId = []
    PolyPointList = []
    IsObjectHave = []
    Reverse = []
    for line in Lines:
        sayac+=1
        if not (sayac == len(Lines) or sayac == 1):
            json_acceptable_string = str(line).replace("'", "\"")

            if json_acceptable_string[-2] == ",":
                json_acceptable_string = json_acceptable_string[: -2]
            # print(json_acceptable_string)
            ClassId.append(json.loads(json_acceptable_string)["ClassId"])
            IsObjectHave.append(json.loads(json_acceptable_string)["IsObjectHave"])
            Reverse.append(json.loads(json_acceptable_string)["Reverse"])
            res.append(json.loads(json_acceptable_string)["PolyPointList"])
            point = []
            for i in res[0]:
                x = i["X"]
                y = i["Y"]
                point.append([x, y])
            PolyPointList.append(point)

    return ClassId, PolyPointList, IsObjectHave, Reverse


# filepath = 'C:/Users/ozan.akyel/Desktop/PlastikRealTime1/rois-Copy.json'
# ClassId, PolyPointList, IsObjectHave, Reverse = get_rois(filepath)
# print(PolyPointList)
