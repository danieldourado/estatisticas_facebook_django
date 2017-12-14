from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='list'),
    url(r'^new/$', views.PostCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.PostDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.PostUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.PostDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/create/$', views.PostCreateView, name='create'),
    url(r'^(?P<pk>\d+)/list/$', views.PostList.as_view(), name='list'),
]
