from django.urls import path, re_path
from . import views

# Django 서버로 Http 요청이 들어올 때마다,
# URLConf 매핑 List 를 처음부터 끝까지 순차적으로 훝으며 검색

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    # re_path(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    re_path(r'^post/(?P<pk>\d+)/comment/new/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^post/(?P<pk>\d+)/comment/(?P<comment_pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    re_path(r'^post/(?P<pk>\d+)/comment/(?P<comment_pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
