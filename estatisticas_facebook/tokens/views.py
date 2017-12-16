from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import TokenForm
from .models import Token


class TokenList(ListView):
    model = Token
    paginate_by = 20


class TokenCreate(CreateView):
    model = Token
    form_class = TokenForm
    success_url = reverse_lazy('tokens:list')


class TokenDetail(DetailView):
    model = Token


class TokenUpdate(UpdateView):
    model = Token
    form_class = TokenForm
    success_url = reverse_lazy('tokens:list')


class TokenDelete(DeleteView):
    model = Token
    success_url = reverse_lazy('tokens:list')
