from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.CommentList.as_view(), name='list'),
    url(r'^new/$', views.CommentCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.CommentDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.CommentUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.CommentDelete.as_view(), name='delete'),
]
