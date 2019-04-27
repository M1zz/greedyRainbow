from django.db import models


# Create your models here.
class Tasks(models.Model):
    username = models.CharField(max_length=200)
    task_start = models.DateTimeField()
    task_end = models.DateTimeField()
