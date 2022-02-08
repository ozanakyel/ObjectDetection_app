from . import views
from django.urls import re_path

urlpatterns = [
    re_path('get_projects', views.get_projects),
    re_path('video_feed', views.video_feed),
    re_path('video_feed_object_detection', views.video_feed_object_detection)
]