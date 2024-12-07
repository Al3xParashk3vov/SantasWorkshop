from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from SantasWorkshop.accounts.views import UserRegisterView, ProfileDetailView, ProfileEditView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('details/', ProfileDetailView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
    ]))
]