from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from core.models import Location

# Create your views here.
class Posts(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/posts.html"

class PostsByLocation(generic.ListView):
    template_name = "blog/posts.html"
    context_object_name = 'posts'

    def get_queryset(self):
        location_slug = self.kwargs.get('location_slug')
        location = get_object_or_404(Location, slug=location_slug)
        return Post.objects.filter(location=location)
  
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter()
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )




