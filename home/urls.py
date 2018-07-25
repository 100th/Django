from django.urls import path, re_path
from .views import home

urlpatterns = [
    re_path(r'^$', home, name='home'),
]
