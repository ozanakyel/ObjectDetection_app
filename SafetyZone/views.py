import re
from django.shortcuts import render
from datetime import date, datetime,timedelta
from django.http.response import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from SafetyZone.camera import VideoCamera, gen

from SafetyZone.models import Project, Config, ProjectConfig
from SafetyZone.serializers import ProjectSerializer,ConfigSerializer,ProjectConfigSerializer

# cam = VideoCamera()

# configkeys = Config.objects.all().values()
# for item in configkeys:
#     print(item)

@csrf_exempt
def video_feed(request):
	return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")

@csrf_exempt
def get_projects(request, id = 0):
    if request.method == "GET":
        projects = Project.objects.all()
        projects_serializer = ProjectSerializer(projects, many = True)
        return JsonResponse(projects_serializer.data, safe=False)