from bson import ObjectId
from django.db import models
import mongoengine


# Create your models here.

class UserModel(models.Model):
    video = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=500)

    class Meta:
        db_table = 'db'