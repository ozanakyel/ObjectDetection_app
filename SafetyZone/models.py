from django.db import models

class Project(models.Model):
    cityID = models.AutoField(primary_key=True)
