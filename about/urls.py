from django.urls import path, re_path
from .views import about

urlpatterns = [
    re_path(r'^$', about, name='about'),
]
