from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from pages.models import *
from estatisticas_facebook.posts.models import Post
import facebook
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .forms import *
from django.core.urlresolvers import reverse
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

def ErasePage(request, id):
    Page.objects.get(id__iexact=id).delete()
    return HttpResponseRedirect(reverse('pages:list'));
    
class PageDetailView(DetailView):
   
    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        print(self.kwargs.get("pk"))
        context['page_insights'] = PageInsights.objects.filter(page__id__iexact=self.kwargs.get("pk")).count()
        context['posts'] = Post.objects.filter(page__id__iexact=self.kwargs.get("pk")).count()
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
        return reverse('pages:detail',args=(self.object.id,))

def PageInsightsListView(request, id):
    template_name = 'pages/pageinsights_list.html'
    page_name = Page.objects.get(id__iexact = id).pretty_name

    queryset = PageInsights.objects.filter(Q(page__id__iexact=id))
    
    
    table = PageInsightsTable(queryset)

    RequestConfig(request).configure(table)
    
    return render(request, 'pages/pageinsights_list.html', {'table': table, 'page_name': page_name, 'id':id})


def PageInsightsCreateView(request, **kwargs):
    form = PageInsightsCreateForm(request.POST or None)
    template_name = 'pages/pageinsights_form.html'
    errors = None
    if form.is_valid():
        args = kwargs
        args['since'] = form.cleaned_data.get('since')
        getPageInsights(args)
        
        return HttpResponseRedirect(reverse('pages:detail',kwargs={'pk': kwargs['id']}));
    
    if form.errors:
        errors = form.errors
    
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)

class PageInsightsDetailView(DetailView):
    queryset = PageInsights.objects.all()

