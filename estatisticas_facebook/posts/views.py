from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import PostForm
from .models import Post


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


class PostCreatet(CreateView):
    model = Post
    success_url = reverse_lazy('posts:list')
