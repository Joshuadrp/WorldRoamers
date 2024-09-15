from django.db import models
from django.contrib.auth.models import User

class MyProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    name = models.CharField(max_length=200, unique=True, blank=True, default='')  # Default value
    surname = models.CharField(max_length=200, unique=True, blank=True, default='')  # Default value
    profile_picurl = models.CharField(max_length=200, blank=True)
    countries_visited = models.CharField(max_length=200, blank=True, default='How many?!')  # Default value
    interests = models.CharField(max_length=200, blank=True, default='Do you have any?')  # Default value

    def __str__(self):
        return str(self.user)
