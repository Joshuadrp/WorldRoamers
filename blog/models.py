from django.db import models
from django.contrib.auth.models import User
from core.models import Location
from cloudinary.models import CloudinaryField
from django.utils.text import slugify



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    blog_img = CloudinaryField('image', blank=True, null=True)
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

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