from django.db import models


# Create your models here.

class Permission(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    is_active = models.BooleanField()

class User(models.Model):
    username = models.CharField(max_length=50)
    permission_id = models.CharField(max_length=100)
    
    
