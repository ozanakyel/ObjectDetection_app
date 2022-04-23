from asyncio import tasks
import re
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
    # if item['cameraIP'] == '0':
    #     running_projects.append(VideoCamera())
    # else:
    #     running_projects.append(VideoCamera(item['cameraIP']))



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
            running_projects.append(VideoCamera())
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)
@csrf_exempt
def get_configs(request, id = 0):
    if request.method == "GET":
        configs = Config.objects.all()
        configs_serializer = ConfigSerializer(configs, many = True)
        return JsonResponse(configs_serializer.data, safe=False)
    elif request.method == 'POST':
        projects_data = JSONParser().parse(request)
        patient_serializer = ProjectSerializer(data = projects_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            running_projects.append(VideoCamera())
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)