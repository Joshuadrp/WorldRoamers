import random
import factory
from django.contrib.auth.models import User
from .models import Post
from core.models import Location

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = 'tester'
    email = 'tester@example.com'
    password = factory.PostGenerationMethodCall('set_password', 'password123')


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location
        django_get_or_create = ('name',)

    name = factory.Iterator(['Europe', 'Asia', 'Oceania', 'America', 'Africa'])


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence', nb_words=6)
    slug = factory.Faker('slug')
    content = factory.Faker('paragraph', nb_sentences=10)
    author = factory.SubFactory(UserFactory)
    img_url = factory.Faker('image_url')
    location = factory.SubFactory(LocationFactory)
