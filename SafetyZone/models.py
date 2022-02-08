from django.db import models

class Project(models.Model):
    projectID = models.AutoField(primary_key=True)
