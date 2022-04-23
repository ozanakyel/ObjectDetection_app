from . import views
from django.urls import re_path, path

urlpatterns = [
    re_path('get_projects', views.get_projects),
    re_path('get_configs', views.get_configs),
    path('video_feed/<int:id>/', views.video_feed),
    path('object_detection/<int:id>/', views.video_feed_object_detection),
    path('video_feed_single/<int:id>/', views.video_feed_single),
    path('object_detection_single/<int:id>/', views.video_feed_object_detection_single),
    path('test/<int:id>/', views.test),
]