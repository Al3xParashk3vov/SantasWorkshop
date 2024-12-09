from django.urls import path

from SantasWorkshop.base import views
from SantasWorkshop.base.views import index, DashboardView

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', DashboardView.as_view(), name='dash'),
]
