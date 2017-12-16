from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import FaceUsersForm
from .models import FaceUsers


class FaceUsersList(ListView):
    model = FaceUsers
    paginate_by = 20


class FaceUsersCreate(CreateView):
    model = FaceUsers
    form_class = FaceUsersForm
    success_url = reverse_lazy('faceusers:list')


class FaceUsersDetail(DetailView):
    model = FaceUsers


class FaceUsersUpdate(UpdateView):
    model = FaceUsers
    form_class = FaceUsersForm
    success_url = reverse_lazy('faceusers:list')


class FaceUsersDelete(DeleteView):
    model = FaceUsers
    success_url = reverse_lazy('faceusers:list')
