from django.db import models

class Project(models.Model):
    projectID = models.AutoField(primary_key=True)
    plant = models.IntegerField(null=True)
    name = models.CharField(max_length=200)
    cameraIP = models.CharField(max_length=200)
    cameraType = models.CharField(max_length=200)
    userName = models.CharField(max_length=200)
    userPassword = models.CharField(max_length=200)

class Config(models.Model):
    configKeyID = models.AutoField(primary_key=True)
    configKey = models.CharField(max_length=200)

class ConfigKeyValues(models.Model):
    projectID = models.ForeignKey(Project, default= None, on_delete=models.CASCADE)
    configKeyID = models.ForeignKey(Config, default= None, on_delete=models.CASCADE)
    configValue = models.CharField(max_length=200, null=True)
