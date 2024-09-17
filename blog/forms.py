from django import forms
from .models import Comment,Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'blog_img', 'location']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'blog_img', 'location']


