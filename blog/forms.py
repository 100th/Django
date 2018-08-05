from django import forms
from .models import Post, Comment
from mysite.widgets.naver_map_point_widget import NaverMapPointWidget
from .widgets import CounterTextInput, RateitjsWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'      # ['title', 'text', 'lnglat']
        widgets = {
            'lnglat' : NaverMapPointWidget(),
            'rating': RateitjsWidget,
            'title' : CounterTextInput,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
