from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
]
