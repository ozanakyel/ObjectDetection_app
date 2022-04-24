from django.db.models import fields
from rest_framework import serializers
from SafetyZone.models import *

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields=('projectID', 'plant', 'name', 'cameraIP', 'cameraType', 'userName', 'userPassword', 'modelName')

class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Config
        fields=('configKeyID', 'configName')
        
class ProjectConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConfigValue
        fields=('projectID_id', 'configKeyID_id', 'configValue')

        