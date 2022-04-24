from asyncio import tasks
import re
from tokenize import Number
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
import threading
from SafetyZone.camera import VideoCamera

from SafetyZone.models import *
from SafetyZone.serializers import ProjectSerializer,ConfigSerializer,ProjectConfigSerializer


running_projects = []
for item in Project.objects.all().values():
    print(item, item['cameraIP'])
    if item['cameraIP'] == '0':
        running_projects.append(VideoCamera(item['name'],item['modelName']))
    else:
        running_projects.append(VideoCamera(item['name'], item['modelName'], item['cameraIP']))



@csrf_exempt
def test(request, id=0):
    if request.method == "GET":
        print(id, request)
        return JsonResponse("Added Successfully", safe = False)

@csrf_exempt
def video_feed(request, id=0):
    return StreamingHttpResponse(running_projects[id].gen(), content_type="multipart/x-mixed-replace;boundary=frame")


@csrf_exempt
def video_feed_object_detection(request, id=0):
	return StreamingHttpResponse(running_projects[id].gen2(), content_type="multipart/x-mixed-replace;boundary=frame")

@csrf_exempt
def video_feed_single(request, id=0):
    return StreamingHttpResponse(running_projects[id].gen_single(), content_type="multipart/x-mixed-replace;boundary=frame")


@csrf_exempt
def video_feed_object_detection_single(request, id=0):
	return StreamingHttpResponse(running_projects[id].gen2_single(), content_type="multipart/x-mixed-replace;boundary=frame")



@csrf_exempt
def get_projects(request, id = 0):
    if request.method == "GET":
        projects = Project.objects.all()
        projects_serializer = ProjectSerializer(projects, many = True)
        return JsonResponse(projects_serializer.data, safe=False)
    elif request.method == 'POST':
        projects_data = JSONParser().parse(request)
        patient_serializer = ProjectSerializer(data = projects_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            if projects_data['cameraIP'] == '0':
                running_projects.append(VideoCamera(projects_data['name'],projects_data['modelName']))
            else:
                running_projects.append(VideoCamera(projects_data['name'], projects_data['cameraIP'], projects_data['modelName']))
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)
@csrf_exempt
def get_configs(request, id = 0):
    if request.method == "GET":
        configs = Config.objects.all()
        configs_serializer = ConfigSerializer(configs, many = True)
        return JsonResponse(configs_serializer.data, safe=False)
    elif request.method == 'PUT':
        configs_data = JSONParser().parse(request)
        config = ConfigValue.objects.filter(projectID = configs_data['projectID_id'], configKeyID = configs_data['configKeyID_id']).first()
        if config == None:
            config = Config.objects.get(configKeyID = int(configs_data['configKeyID_id']))
            project = Project.objects.get(projectID = int(configs_data['projectID_id']))
            configs_serializer = ConfigValue(projectID = project, configKeyID = config, configValue = configs_data['configValue'])
            configs_serializer.save()
            return JsonResponse("Updated Successfully", safe = False)
        else:
            configs_serializer = ProjectConfigSerializer(config, data = configs_data)
            if configs_serializer.is_valid():
                configs_serializer.save()
                # project = Project.objects.filter(projectID = int(configs_data['projectID_id'])).values()[0]
                # print(project)
                # for i in range(len(running_projects)):
                #     if project['name'] == running_projects[i].project_name:
                #         running_projects.pop(i)
                #         del running_projects[i]
                #         print(running_projects)
                        # if project['cameraIP'] == '0':
                        #     running_projects.append(VideoCamera(project['name']))
                        # else:
                        #     running_projects.append(VideoCamera(project['name'], project['cameraIP']))
                return JsonResponse("Updated Successfully", safe = False)
            else:
                print(configs_serializer.errors)
        return JsonResponse("Failed to Update", safe = False)