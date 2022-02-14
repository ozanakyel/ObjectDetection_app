from asyncio import tasks
import re
from django.shortcuts import render
from datetime import date, datetime,timedelta
from django.http.response import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from SafetyZone.camera import VideoCamera,gen, gen2
import requests
import cv2

from SafetyZone.models import Project, Config, ProjectConfig
from SafetyZone.serializers import ProjectSerializer,ConfigSerializer,ProjectConfigSerializer
from celery import shared_task

# videocamera = cv2.VideoCapture(0)
cam = VideoCamera() 

@csrf_exempt
def video_feed(request):
    return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")

@csrf_exempt
def video_feed_object_detection(request):
	return StreamingHttpResponse(gen2(cam), content_type="multipart/x-mixed-replace;boundary=frame")

@csrf_exempt
def get_projects(request, id = 0):
    if request.method == "GET":
        projects = Project.objects.all()
        projects_serializer = ProjectSerializer(projects, many = True)
        return JsonResponse(projects_serializer.data, safe=False)
    # return JsonResponse("asd", safe=False)
# requests.get('http://127.0.0.1:8000/video_feed')
# requests.get('http://127.0.0.1:8000/object_detection')
# threading.Thread(target=video_feed, args=(1), daemon=True).start()
# threading.Thread(target=video_feed_object_detection, args=(1), daemon=True).start()