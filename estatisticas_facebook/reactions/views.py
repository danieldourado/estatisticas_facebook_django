from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ReactionForm
from .models import Reaction


class ReactionList(ListView):
    model = Reaction
    paginate_by = 20


class ReactionCreate(CreateView):
    model = Reaction
    form_class = ReactionForm
    success_url = reverse_lazy('reactions:list')


class ReactionDetail(DetailView):
    model = Reaction


class ReactionUpdate(UpdateView):
    model = Reaction
    form_class = ReactionForm
    success_url = reverse_lazy('reactions:list')


class ReactionDelete(DeleteView):
    model = Reaction
    success_url = reverse_lazy('reactions:list')
