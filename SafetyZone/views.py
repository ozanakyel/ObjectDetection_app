import re
from django.shortcuts import render
from datetime import date, datetime,timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from SafetyZone.models import Project, Config, ProjectConfig
from SafetyZone.serializers import ProjectSerializer,ConfigSerializer,ProjectConfigSerializer