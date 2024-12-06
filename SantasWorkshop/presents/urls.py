from django.urls import path, include

from SantasWorkshop.presents import views
from SantasWorkshop.presents.views import PhotoAddPage

urlpatterns = [
    path('add/', PhotoAddPage.as_view(), name='add_present'),
    path('<int:pk>/', include([
        path('', views.PhotoDetailsView.as_view(), name='photo-details'),
        path('edit/', views.PhotoEditPage.as_view(), name='photo-edit'),
        path('delete/', views.photo_delete, name='photo-delete'),
    ])),
]
