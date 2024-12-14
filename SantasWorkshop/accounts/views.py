from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from SantasWorkshop.accounts.forms import CustomUserForm, ProfileEditForm
from SantasWorkshop.accounts.models import Profile
from SantasWorkshop.presents.models import Present
from SantasWorkshop.review.models import KidStatus

UserModel = get_user_model()

# Create your views here.
class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        if get_user_model().objects.filter(username=username).exists():
            form.add_error('username', 'Username already exists')
            return self.form_invalid(form)

        return super().form_valid(form)

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'profiles/profile-details-page.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.object

        # Get or create kid status
        kid_status, created = KidStatus.objects.get_or_create(
            user=self.object,
            defaults={'status': 'GOOD'}
        )
        context['kid_status'] = kid_status

        # Add status choices if user is staff
        if self.request.user.is_staff:
            context['status_choices'] = KidStatus.STATUS_CHOICES

        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_staff:
            self.object = self.get_object()
            kid_status = KidStatus.objects.get_or_create(user=self.object)[0]
            new_status = request.POST.get('status')

            if new_status in dict(KidStatus.STATUS_CHOICES):
                kid_status.status = new_status
                kid_status.save()
                messages.success(request, f"Status updated to {kid_status.get_status_display()}")

        return self.get(request, *args, **kwargs)

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        # Get or create profile for the current user
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete-page.html'
    success_url = reverse_lazy('login')

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user


class ProfilePresentsDashboard(LoginRequiredMixin, ListView):
    model = Present
    template_name = 'profiles/profile-presents-page.html'
    context_object_name = 'presents'
    paginate_by = 6  # Optional: adds pagination for many presents

    def get_queryset(self):
        return Present.objects.filter(user_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_presents'] = self.get_queryset().count()
        return context