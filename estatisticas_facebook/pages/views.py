from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from pages.models import Page, PageInsights
import facebook
import json
from django.http import HttpResponse
from django.db.models import Q
from .forms import PageCreateForm
from django.core.urlresolvers import reverse
from pages.facebook_crawler import getPageInfo

# Create your views here.

class PageView(TemplateView):
    
    def get_context_data(self, *args, **kwargs):
        context = super(PageView, self).get_context_data(*args, **kwargs)
        return context

def eraseAllPageinsights(request):
    return eraseModelAndReturnHttpResponse(PageInsights)

def eraseAllPages(request):
    return eraseModelAndReturnHttpResponse(Page)

def eraseModelAndReturnHttpResponse(model):
    model.objects.all().delete()
    return HttpResponse("Quantidade de dados na tabela: "+str(model.objects.all().count()))


class PageDetailView(DetailView):
   
    template_name = 'pages/page_detail.html'
   
    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = queryset = Page.objects.filter(slug__iexact=slug)
        else:
            queryset = Page.objects.all()
        return queryset

class PageListView(ListView):
    template_name = 'pages/page_list.html'
    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = queryset = Page.objects.filter(slug__iexact=slug)
        else:
            queryset = Page.objects.all()
        return queryset
    
    queryset = Page.objects.all()

class PageCreateView(CreateView):
    form_class = PageCreateForm
    template_name = 'pages/form.html'
    def get_success_url(self):
        getPageInfo(self.object)
        return reverse('pages:detail',args=(self.object.slug,))
   

class PageInsightsListView(ListView):
    template_name = 'pages/pageinsights_list.html'
    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = PageInsights.objects.filter(
                Q(page__slug__iexact=slug)
            )
        else:
            queryset = PageInsights.objects.none()
        return queryset

class PageInsightsDetailView(DetailView):
    queryset = PageInsights.objects.all()

class PageInsightsExtractView(ListView):    
    model = Page
    #template_name = "estatisticas_facebook/page_detail.html"
    
    def get_context_data(self, **kwargs):
        
        context = super(PageExtractView, self).get_context_data( **kwargs)
        pagename = Page.objects.get(pk=self.kwargs['pk'])
  
        #token = 'EAACEdEose0cBAD6KsQvpVng9vUXf2xzVVTZAX2BwoX3bpRRg9RIfZAg88V3ZBT3P8nrDdiND9TuqN6E4fUhI27WOeATc8ZCRXFttxWt4dFrZCweSJg5Qx0ZCtaRLRa93HDuyZADKDRkb95DqOtbsqXmOMhaoZBbj0qQXgXw7hlZC7I4n37u1m7eKkimGThgWBtNIZD'
        token = Page.objects.get(pk=self.kwargs['pk']).access_token
        since = Page.objects.get(pk=self.kwargs['pk']).since
        graph = facebook.GraphAPI(token)

        raw_json = graph.get_object(pagename.name+'/insights?period=day&metric=page_fan_adds_unique,page_impressions_unique,page_engaged_users,page_stories,page_storytellers&since='+str(since))
        pagedata = raw_json['data']

        for obj in pagedata:
            print (obj['name'])
            for value in obj['values']:
                page_insights = PageInsights(
                    name=obj['name'], 
                    period=obj['period'], 
                    title=obj['title'], 
                    description=obj['description'], 
                    end_time=value['end_time'], 
                    value=value['value'], 
                    page_id=self.kwargs['pk'])
                page_insights.save()
        return context