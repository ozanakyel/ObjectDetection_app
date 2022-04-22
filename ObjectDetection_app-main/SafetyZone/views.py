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


# videocamera = cv2.VideoCapture(0)
cam = VideoCamera() 


# def video_stream_orj():
#     return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
# threading.Thread(target=video_stream_orj, args=(), daemon=True).start()

@csrf_exempt
def video_feed(request):
    # print(request.__dict__)
    return StreamingHttpResponse(cam.gen(), content_type="multipart/x-mixed-replace;boundary=frame")
# threading.Thread(target=video_feed, args=('asd'), daemon=True).start()

@csrf_exempt
def video_feed_object_detection(request):
	return StreamingHttpResponse(cam.gen2(), content_type="multipart/x-mixed-replace;boundary=frame")

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