from django.db.models import fields
from rest_framework import serializers
from SafetyZone.models import *

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields=('projectID', 'plant', 'name', 'cameraIP', 'cameraType', 'userName', 'userPassword')

class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Config
        fields=('configKeyID', 'configKey')
        
class ProjectConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConfigKeyValues
        fields=('projectID', 'configKeyID', 'configValue')