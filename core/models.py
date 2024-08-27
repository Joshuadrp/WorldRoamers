from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

