from django.conf.urls import url

from pages.views import *

urlpatterns = [

    url(
        regex=r'^create/$',
        view= PageCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^detail/(?P<slug>[\w-]+)/$',
        view= PageDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^page/extract/(?P<pk>\w+)/$',
        view= PageExtractView.as_view(),
        name='extract'
    ),
    url(
        regex=r'^page/insights/erase-all/',
        view= eraseAllPageinsights,
        name='erase-all-insights'
    ),
    url(
        regex=r'^page/insights/(?P<slug>[\w-]+)/$',
        view= PageInsightsListView.as_view(),
        name='insights-list'
    ),
    url(
        regex=r'^page/erase-all/',
        view= eraseAllPages,
        name='erase-all-pages'
    ),
    url(
        regex=r'^page/(?P<slug>[\w-]+)/$',
        view= PageListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^page/',
        view= PageListView.as_view(),
        name='list'
    ),
    #url(r'^page/insights/$', PageInsightsListView.as_view()),
    
    #url(r'^page/index/(?P<slug>\w+)/$', PageListView.as_view()),
]