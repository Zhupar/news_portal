from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_author', 'post_choice', 'post_category', 'post_title', 'post_text']
