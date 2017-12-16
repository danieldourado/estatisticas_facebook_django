from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.TokenList.as_view(), name='list'),
    url(r'^new/$', views.TokenCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.TokenDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.TokenUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.TokenDelete.as_view(), name='delete'),
]
