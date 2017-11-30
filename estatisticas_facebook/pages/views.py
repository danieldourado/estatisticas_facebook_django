from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from pages.models import Page, PageInsights
import facebook
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .forms import *
from django.core.urlresolvers import reverse
from pages.facebook_crawler import *
from .tables import *
from django_tables2 import RequestConfig

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

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        print(self.kwargs.get("pk"))
        context['page_insights'] = PageInsights.objects.filter(page__id__iexact=self.kwargs.get("pk")).count()
        print(context)
        return context
        
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if pk:
            queryset = queryset = Page.objects.filter(id__iexact=pk)
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
        return reverse('pages:detail',args=(self.object.slug,))

def PageInsightsListView(request, id):

    page_name = Page.objects.get(id__iexact = id).pretty_name
    
    queryset = PageInsights.objects.filter(Q(page__id__iexact=id))
    table = PageInsightsTable(queryset)

    RequestConfig(request).configure(table)
    
    return render(request, 'pages/pageinsights_list.html', {'table': table, 'page_name': page_name})


def PageInsightsCreateView(request, **kwargs):
    form = PageInsightsCreateForm(request.POST or None)
    template_name = 'pages/pageinsights_form.html'
    errors = None
    if form.is_valid():
        args = kwargs
        args['since'] = form.cleaned_data.get('since')
        args['access_token'] = form.cleaned_data.get('access_token')
        getPageInsights(args)
        
        return HttpResponseRedirect(reverse('pages:detail',kwargs={'pk': kwargs['id']}));
    
    if form.errors:
        errors = form.errors
    
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)

class PageInsightsDetailView(DetailView):
    queryset = PageInsights.objects.all()

class PageInsightsExtractView(ListView):    
    model = Page
    #template_name = "estatisticas_facebook/page_detail.html"
    
    def get_context_data(self, **kwargs):
        
        context = super(PageInsightsExtractView, self).get_context_data( **kwargs)
        pagename = Page.objects.get(pk=self.kwargs['pk'])
  
        #token = 'EAACEdEose0cBAD6KsQvpVng9vUXf2xzVVTZAX2BwoX3bpRRg9RIfZAg88V3ZBT3P8nrDdiND9TuqN6E4fUhI27WOeATc8ZCRXFttxWt4dFrZCweSJg5Qx0ZCtaRLRa93HDuyZADKDRkb95DqOtbsqXmOMhaoZBbj0qQXgXw7hlZC7I4n37u1m7eKkimGThgWBtNIZD'
        token = Page.objects.get(pk=self.kwargs['pk']).access_token
        since = Page.objects.get(pk=self.kwargs['pk']).since
        graph = facebook.GraphAPI(token)
        return
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