from django.urls import path

from SantasWorkshop.base import views
from SantasWorkshop.base.views import index, DashboardView, about, story

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('story/', story, name='story'),

    path('dashboard/', DashboardView.as_view(), name='dash'),
]
