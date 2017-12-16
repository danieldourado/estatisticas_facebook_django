from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.FaceUsersList.as_view(), name='list'),
    url(r'^new/$', views.FaceUsersCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.FaceUsersDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.FaceUsersUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.FaceUsersDelete.as_view(), name='delete'),
]
