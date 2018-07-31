from django.conf import settings
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^profile/$', views.profile, name='profile'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': settings.LOGIN_URL}),
]
