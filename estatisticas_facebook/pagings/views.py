from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import PagingForm
from .models import Paging


class PagingList(ListView):
    model = Paging
    paginate_by = 20


class PagingCreate(CreateView):
    model = Paging
    form_class = PagingForm
    success_url = reverse_lazy('pagings:list')


class PagingDetail(DetailView):
    model = Paging


class PagingUpdate(UpdateView):
    model = Paging
    form_class = PagingForm
    success_url = reverse_lazy('pagings:list')


class PagingDelete(DeleteView):
    model = Paging
    success_url = reverse_lazy('pagings:list')
