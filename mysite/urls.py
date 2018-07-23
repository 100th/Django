from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from django.shortcuts import redirect

app_name = 'shop'
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    # re_path(r'^accounts/login/$', login, name='login'), #import에서 안쓰면 views.login 이다.
    re_path(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    re_path(r'^blog/', include('blog.urls')),

    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^shop/', include('shop.urls')),
    re_path(r'^$', lambda request: redirect('shop:index'), name='root'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
