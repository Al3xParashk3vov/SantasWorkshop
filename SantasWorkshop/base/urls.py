from django.urls import path

from SantasWorkshop.base import views
from SantasWorkshop.base.views import index

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
