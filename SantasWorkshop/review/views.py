from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from SantasWorkshop.accounts.models import Profile
from SantasWorkshop.review.models import KidStatus


# Create your views here.
@login_required
def profile_details(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    # Get or create kid status
    kid_status, created = KidStatus.objects.get_or_create(
        user=profile.user,
        defaults={'status': 'GOOD'}
    )

    # Handle status update for staff members
    if request.method == 'POST' and request.user.is_staff:
        new_status = request.POST.get('status')
        if new_status in dict(KidStatus.STATUS_CHOICES):
            kid_status.status = new_status
            kid_status.save()
            messages.success(request, f"Status updated to {kid_status.get_status_display()}")
            return redirect('profile-details', pk=pk)

    context = {
        'profile': profile,
        'kid_status': kid_status,
        'is_staff': request.user.is_staff,
        'status_choices': KidStatus.STATUS_CHOICES,
    }

    return render(request, 'profile_details.html', context)