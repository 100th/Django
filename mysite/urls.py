from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from django.shortcuts import redirect

# 최상위 주소로 바로 가는 법
# 이거 쓰려면 app_name 등록하고 쓸때도 blog:post_list 이런식으로 써야하는듯 하다
# 지금은 굳이 쓸필요 없어서 그냥 놔둠
# def root(request):
#      return redirect('shop:index')

app_name = 'shop'
urlpatterns = [
    # re_path(r'^$', lambda r: redirect('home:home'), name='root'),
    # re_path(r'^$', root, name='root'),    # 아래와 같다
    # re_path(r'^$', lambda r: redirect('blog:post_list'), name='root'),
    # re_path(r'^$', lambda request: redirect('shop:index'), name='root'),
    re_path(r'^', include('home.urls')),
    re_path(r'^admin/', admin.site.urls),
    # re_path(r'^accounts/login/$', login, name='login'),    #import에서 안쓰면 views.login 이다.
    re_path(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^home/', include('home.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^shop/', include('shop.urls')),
    # include 시에는 url pattern 끝에 $ 안붙인다.
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
