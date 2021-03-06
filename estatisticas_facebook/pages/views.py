from django.shortcuts import render
from django.db.models.functions import Coalesce
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from estatisticas_facebook.pages.models import *
from estatisticas_facebook.posts.models import Post
from estatisticas_facebook.comments.models import Comment
from estatisticas_facebook.reactions.models import Reaction
from estatisticas_facebook.faceusers.models import FaceUsers
from util.graph import *
from django.db.models import Q

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
        context['comments'] = Comment.objects.filter(post__page__id__iexact=self.kwargs.get("pk")).count()
        context['reactions'] = Reaction.objects.filter(post__page__id__iexact=self.kwargs.get("pk")).count()
        context['reactions_like'] = Reaction.objects.filter(post__page__id__iexact=self.kwargs.get("pk"), type="LIKE").count()
        context['reactions_love'] = Reaction.objects.filter(post__page__id__iexact=self.kwargs.get("pk"), type="LOVE").count()
        context['reactions_haha'] = Reaction.objects.filter(post__page__id__iexact=self.kwargs.get("pk"), type="HAHA").count()
        context['reactions_wow'] = Reaction.objects.filter(post__page__id__iexact=self.kwargs.get("pk"), type="WOW").count()
        context['reactions_sad'] = Reaction.objects.filter(post__page__id__iexact=self.kwargs.get("pk"), type="SAD").count()
        context['reactions_angry'] = Reaction.objects.filter(post__page__id__iexact=self.kwargs.get("pk"), type="ANGRY").count()
        context['faceusers'] = FaceUsers.objects.all().count()
        context['haters'] = FaceUsers.objects.all().order_by('-post_reactions_angry_total')[:10]
        context['likers'] = FaceUsers.objects.all().order_by('-post_reactions_like_total')[:10]
        context['lovers'] = FaceUsers.objects.all().order_by(Coalesce('post_reactions_love_total','comments').desc())[:10]
        context['sads'] = FaceUsers.objects.all().order_by(Coalesce('post_reactions_sad_total','comments').desc())[:10]
        context['commenters'] = FaceUsers.objects.all().order_by(Coalesce('comments','post_reactions_sad_total').desc())[:10]
        context['reactions_is_complete'] = "Completo"
        if Post.objects.all().exclude(reaction_paging = FINISHED).exists():
            context['reactions_is_complete'] = "Incompleto"
        context['comments_is_complete'] = "Completo"
        if Post.objects.all().exclude(comment_paging = FINISHED).exists():
            context['comments_is_complete'] = "Incompleto"
            
        print(context['reactions_like'])
        
        '''
        from estatisticas_facebook.posts.admin import PostResource
        dataset = PostResource().export()
        print (dataset.csv)    
        '''    
            
            
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

def PageInsightsCreateViewCron(request, **kwargs):
    args = {}
    args['since'] = kwargs['since']
    args['id'] = kwargs['id']
    getPageInsights(args)
    return HttpResponse("Success")

    

class PageInsightsDetailView(DetailView):
    queryset = PageInsights.objects.all()

