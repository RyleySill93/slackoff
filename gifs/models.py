from django.db import models


# Create your models here.
class Image(models.Model):
    s3_key = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000)
    width = models.IntegerField()
    height = models.IntegerField()
