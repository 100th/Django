from django import forms
from .models import Post, Comment
from .widgets import NaverMapPointWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'lnglat']
        widgets = {
            'lnglat' : NaverMapPointWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
