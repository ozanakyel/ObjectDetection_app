from . import views
from django.urls import re_path

urlpatterns = [
    re_path('video_feed', views.video_feed),
]