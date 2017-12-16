from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.PagingList.as_view(), name='list'),
    url(r'^new/$', views.PagingCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.PagingDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.PagingUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.PagingDelete.as_view(), name='delete'),
]
