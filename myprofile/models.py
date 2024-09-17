from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class MyProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    name = models.CharField(max_length=200, unique=True, blank=True)  
    surname = models.CharField(max_length=200, unique=True, blank=True)  
    profile_pic = CloudinaryField('image', default='placeholder')
    countries_visited = models.CharField(max_length=200, blank=True)  
    interests = models.CharField(max_length=200, blank=True) 
    nationality =  models.CharField(max_length=200, blank=True) 

    def __str__(self):
        return str(self.user)
