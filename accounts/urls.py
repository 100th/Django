from django.urls import path, re_path
from django.contrib.auth.views import login, logout
from .views import profile, signup

urlpatterns = [
    re_path(r'^signup/$', signup, name='signup'),
    re_path(r'^profile/$', profile, name='profile'),
    re_path(r'^login/$', login, name='login', kwargs={ 'template_name' : 'accounts/login.html', }),
]
