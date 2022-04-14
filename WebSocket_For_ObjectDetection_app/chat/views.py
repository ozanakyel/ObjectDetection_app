from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import StreamingHttpResponse
from .camera import VideoCamera,gen
# from .websocket_connection import WebSocket
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
# Create your views here.

def lobby(request):
    return render(request, 'chat/lobby.html')


# # cam = VideoCamera() 
# @csrf_exempt
# def video_feed(request):
#     # wssend = WebSocket()
#     # gen(cam, wssend)
#     return HttpResponse("Here's the text of the web page.")
#     # return StreamingHttpResponse(gen(cam, wssend), content_type="multipart/x-mixed-replace;boundary=frame")