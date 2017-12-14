from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import PostForm, PostCreateForm
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


class PostList(ListView):
    model = Post
    paginate_by = 20


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts:list')


class PostDetail(DetailView):
    model = Post


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts:list')


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:list')


def PostCreateView(request, **kwargs):
    form = PostCreateForm(request.POST or None)
    template_name = 'posts/post_form.html'
    errors = None
    if form.is_valid():
        args = kwargs
        args['since'] = form.cleaned_data.get('since')
        args['access_token'] = form.cleaned_data.get('access_token')
        #getPageInsights(args)
        print(args)
        return HttpResponseRedirect(reverse('pages:detail',kwargs={'pk': kwargs['pk']}));
    
    if form.errors:
        errors = form.errors
    
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)