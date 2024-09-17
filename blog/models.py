from django.db import models
from django.contrib.auth.models import User
from core.models import Location
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    blog_img = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE,related_name='posts')
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE,related_name='posts',null=True, blank=True
    )

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Comment(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name='comments',null=True, blank=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',null=True, blank=True
    )

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"written by {self.author}"