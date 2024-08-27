from django.db import models
from django.contrib.auth.models import User
from core.models import Location

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    img_url = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE)
    location_id = models.ForeignKey(
        Location, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"{self.title} | written by {self.author}"