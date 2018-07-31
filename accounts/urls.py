from django.conf import settings
from django.urls import path, re_path
from django.contrib.auth.views import login, logout
from .views import profile, signup
from .forms import LoginForm

urlpatterns = [
    re_path(r'^signup/$', signup, name='signup'),
    re_path(r'^profile/$', profile, name='profile'),
    re_path(r'^login/$', login, name='login',
        kwargs={'authentication_form' : LoginForm,
                'template_name' : 'accounts/login_form.html', }),
    re_path(r'^logout/$', logout, name='logout', kwargs={'next_page': settings.LOGIN_URL}),
]
