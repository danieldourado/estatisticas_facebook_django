from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import CommentForm
from .models import Comment


class CommentList(ListView):
    model = Comment
    paginate_by = 20


class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('comments:list')


class CommentDetail(DetailView):
    model = Comment


class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('comments:list')


class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('comments:list')
