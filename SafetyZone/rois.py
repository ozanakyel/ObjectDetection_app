import matplotlib.pyplot as plt
import json
import ast

def get_rois(file_path):

with open(file_path, 'r') as j:
    Lines = j.readlines()

sayac = 0    
dictionerys = []
for line in Lines:
    sayac+=1
    if not (sayac == len(Lines) or sayac == 1):
        json_acceptable_string = str(line).replace("'", "\"")
        dictionerys.append(json_acceptable_string)
    
res = []
for item in dictionerys:
    res.append(json.loads(item))
    
return res