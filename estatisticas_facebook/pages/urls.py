from django.conf.urls import url

from estatisticas_facebook.pages.views import *

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
        regex=r'^page/erase/(?P<id>\w+)/$',
        view= ErasePage,
        name='erase-page'
    ),
    url(
        regex=r'^page/',
        view= PageListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^page_insights/create/(?P<id>\w+)/$',
        view= PageInsightsCreateView,
        name='insights-create'
    ),
    url(
        regex=r'^page_insights/(?P<id>\w+)/$',
        view= PageInsightsListView,
        name='insights-list'
    ),
    url(
        regex=r'^page_insights/erase-all/',
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