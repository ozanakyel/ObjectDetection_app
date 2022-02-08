from . import views
from django.urls import re_path

urlpatterns = [
    re_path('get_projects', views.get_projects),
    re_path('video_feed', views.video_feed)
]