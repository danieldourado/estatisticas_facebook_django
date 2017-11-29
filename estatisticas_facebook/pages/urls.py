from django.conf.urls import url

from pages.views import *

urlpatterns = [

    url(
        regex=r'^create/$',
        view= PageCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^detail/(?P<pk>[\w-]+)/$',
        view= PageDetailView.as_view(),
        name='detail'
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
    url(
        regex=r'^pageInsights/create/(?P<id>\w+)/$',
        view= PageInsightsCreateView,
        name='insights-create'
    ),
    url(
        regex=r'^pageInsights/extract/(?P<id>\w+)/$',
        view= PageInsightsExtractView.as_view(),
        name='insights-extract'
    ),
    url(
        regex=r'^pageInsights/(?P<id>\w+)/$',
        view= PageInsightsListView.as_view(),
        name='insights-list'
    ),
    url(
        regex=r'^pageInsights/erase-all/',
        view= eraseAllPageinsights,
        name='erase-all-insights'
    ),
    url(
        regex=r'^page/erase-all/',
        view= eraseAllPages,
        name='erase-all-pages'
    ),
    #url(r'^page/insights/$', PageInsightsListView.as_view()),
    
    #url(r'^page/index/(?P<slug>\w+)/$', PageListView.as_view()),
]