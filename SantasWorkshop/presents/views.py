from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from SantasWorkshop.presents.forms import PresentAddForm
from SantasWorkshop.presents.models import Present


# Create your views here.

class PhotoAddPage(LoginRequiredMixin, CreateView):
    model = Present
    template_name = 'presents/present-add-page.html'
    form_class = PresentAddForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        present = form.save(commit=False)
        present.user = self.request.user

        return super().form_valid(form)
