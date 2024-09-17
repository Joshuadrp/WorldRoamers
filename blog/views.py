from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Post, Comment
from core.models import Location
from .forms import CommentForm

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
    Display an individual :model:`blog.Post` and handle comment submission.
    """
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by("-created_on")

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments, "form": form},
    )


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)

    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', slug=comment.post.slug)
    
    return render(request, 'blog/edit_comment.html', {'form': CommentForm(instance=comment), 'comment': comment})





