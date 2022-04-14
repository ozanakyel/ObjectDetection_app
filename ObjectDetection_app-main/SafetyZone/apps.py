from django.apps import AppConfig
import requests

class SafetyzoneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SafetyZone'
    # def ready(self):
    #     # requests.get('http://127.0.0.1:8000/video_feed')
    #     # requests.get('http://127.0.0.1:8000/object_detection')
    #     print("**************************************************")
    #     # pass
