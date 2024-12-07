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
from django.shortcuts import redirect, render

from SantasWorkshop.presents.forms import PresentAddForm


@login_required
def present_add_page(request):
    if request.method == 'POST':
        form = PresentAddForm(request.POST, request.FILES)
        if form.is_valid():
            present = form.save(commit=False)
            present.user = request.user
            present.save()
            return redirect('index')
    else:
        form = PresentAddForm()
    return render(request, 'presents/present-add-page.html', {'form': form})
