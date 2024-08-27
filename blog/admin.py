from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug',)
    search_fields = ['title',]
    list_filter = ('created_on', 'updated_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('content', 'post',)
    summernote_fields = ('content',)



