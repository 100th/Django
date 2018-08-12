from django.urls import path, re_path
from .views import projects

urlpatterns = [
    re_path(r'^$', projects, name='projects'),
]
