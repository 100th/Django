from django.urls import path, re_path
from . import views

app_name = 'shop'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<item_id>\d+)/order/new/$', views.order_new, name='order_new'),
]
