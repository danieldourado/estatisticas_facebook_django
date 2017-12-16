from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ReactionList.as_view(), name='list'),
    url(r'^new/$', views.ReactionCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.ReactionDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.ReactionUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ReactionDelete.as_view(), name='delete'),
]
