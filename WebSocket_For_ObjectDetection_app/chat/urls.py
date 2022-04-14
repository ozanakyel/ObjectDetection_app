from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.lobby)
    # path('video_feed', views.video_feed)
]