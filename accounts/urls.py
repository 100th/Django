from django.urls import path, re_path
from django.contrib.auth.views import login, logout
from .views import profile

urlpatterns = [
    re_path(r'^login/$', login, name='login', kwargs={ 'template_name' : 'accounts/login.html', }),
    re_path(r'^profile/$', profile, name='profile'),
]
