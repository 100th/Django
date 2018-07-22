from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.views import login, logout

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/login/$', login, name='login'), #import에서 안쓰면 views.login 이다.
    re_path(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    re_path(r'^blog/', include('blog.urls')),
]
