from django import forms
from .models import Post, Comment
from mysite.widgets.naver_map_point_widget import NaverMapPointWidget
from .widgets import CounterTextInput, RateitjsWidget, AutoCompleteSelect, DatePickerWidget, PreviewClearableFileInput, TuiEditorWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'rating', 'when', 'text', 'photo', 'tags', 'lnglat']
        widgets = {
            'lnglat' : NaverMapPointWidget(),
            'rating': RateitjsWidget,
            'title' : CounterTextInput,
            'country': AutoCompleteSelect,
            'when': DatePickerWidget,
            'photo': PreviewClearableFileInput,
            'user_agent': forms.HiddenInput,
            'text': TuiEditorWidget,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
