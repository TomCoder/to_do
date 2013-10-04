from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    start_time = models.DateTime()
    end_time = models.DateTime()
    modified = models.DateTime(auto_now=True)
    created = models.DateTime(auto_now_add=True)
