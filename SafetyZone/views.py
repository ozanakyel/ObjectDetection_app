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

cam = VideoCamera()

@csrf_exempt
def video_feed(request):
	return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")