from django.urls import path, re_path
from . import views

app_name = 'shop'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]
