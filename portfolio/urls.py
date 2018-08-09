from django.urls import path, re_path
from .views import portfolio

urlpatterns = [
    re_path(r'^$', portfolio, name='portfolio'),
]
