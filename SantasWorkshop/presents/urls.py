from django.urls import path, include

from SantasWorkshop.presents import views

urlpatterns = [
    # path('add/', views.PresentAddPage.as_view(), name='present-add'),
    path('add/', views.present_add_page, name='present-add'),
    # path('<int:pk>/', include([
    #     path('', views.PhotoDetailsView.as_view(), name='photo-details'),
    #     path('edit/', views.PhotoEditPage.as_view(), name='photo-edit'),
    #     path('delete/', views.photo_delete, name='photo-delete'),
    # ])),
]
