from django.urls import path, include

from SantasWorkshop.review.views import profile_details

urlpatterns = [
    path('profile/<int:pk>/', profile_details, name='profile-status'),
]