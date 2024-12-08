# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
#
# from SantasWorkshop.presents.forms import PresentAddForm
# from SantasWorkshop.presents.models import Present
#
#
# # Create your views here.
#
# class PresentAddPage(LoginRequiredMixin, CreateView):
#     model = Present
#     form_class = PresentAddForm
#     template_name = 'presents/present-add-page.html'
#     success_url = reverse_lazy('index')
#
#     def form_valid(self, form):
#         present = form.save(commit=False)
#         present.user = self.request.user.profile
#         present.save()
#         return super().form_valid(form)
#
#     # def get_success_url(self):
#     #     return reverse_lazy('index')
#
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView
#
# from SantasWorkshop.presents.forms import PresentAddForm
# from SantasWorkshop.presents.models import Present
#
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from SantasWorkshop.presents.forms import PresentAddForm
from SantasWorkshop.presents.models import Present


# @login_required
# def present_add_page(request):
#     if request.method == 'POST':
#         form = PresentAddForm(request.POST, request.FILES)
#         if form.is_valid():
#             present = form.save(commit=False)
#             present.user = request.user
#             present.save()
#             return redirect('index')
#     else:
#         form = PresentAddForm()
#     return render(request, 'presents/present-add-page.html', {'form': form})

class PresentAddPage(LoginRequiredMixin, CreateView):
    model = Present
    template_name = 'presents/present-add-page.html'
    form_class = PresentAddForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PresentDetailView(LoginRequiredMixin, DetailView):
    model = Present
    template_name = 'presents/present-details-page.html'
    context_object_name = 'present'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add if the current user is the owner
        context['is_owner'] = self.object.user == self.request.user
        return context

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