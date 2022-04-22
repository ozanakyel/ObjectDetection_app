from . import views
from django.urls import re_path, path

urlpatterns = [
    re_path('get_projects', views.get_projects),
    path('video_feed/<int:id>/', views.video_feed),
    path('object_detection/<int:id>/', views.video_feed_object_detection),
    path('test/<int:id>/', views.test),
]