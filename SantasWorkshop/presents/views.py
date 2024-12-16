from asgiref.sync import sync_to_async
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from SantasWorkshop.presents.forms import PresentAddForm
from SantasWorkshop.presents.models import Present



class PresentAddPage(LoginRequiredMixin, CreateView):
    model = Present
    template_name = 'presents/present-add-page.html'
    form_class = PresentAddForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# LoginRequiredMixin,
class PresentDetailView( DetailView):
    model = Present
    template_name = 'presents/present-details-page.html'
    context_object_name = 'present'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add if the current user is the owner
        context['is_owner'] = self.object.user == self.request.user
        return context

    # async def get_context_data(self, **kwargs):
    #     context = await sync_to_async(super().get_context_data)(**kwargs)
    #     # Add if the current user is the owner
    #     context['is_owner'] = self.object.user == self.request.user
    #     return context
    #
    # # Make the get method async as well
    # async def get(self, request, *args, **kwargs):
    #     self.object = await sync_to_async(self.get_object)()
    #     context = await self.get_context_data(object=self.object)
    #     return self.render_to_response(context)

class PresentEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Present
    template_name = 'presents/present-edit-page.html'
    fields = ['name', 'description', 'image']
    success_url = reverse_lazy('profile-presents')

    def test_func(self):
        present = self.get_object()
        return self.request.user == present.user

    def get_success_url(self):
        return reverse_lazy('profile-presents', kwargs={'pk': self.request.user.pk})


class PresentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Present
    template_name = 'presents/present-delete-page.html'

    def test_func(self):
        present = self.get_object()
        return self.request.user == present.user

    def get_success_url(self):
        return reverse_lazy('profile-presents', kwargs={'pk': self.request.user.pk})