from django.urls import path, include

from SantasWorkshop.presents import views

urlpatterns = [
    path('add/', views.PresentAddPage.as_view(), name='present-add'),
    # path('add/', views.present_add_page, name='present-add'),
    path('<int:pk>/', include([
        path('', views.PresentDetailView.as_view(), name='present-details'),
        path('edit/', views.PresentEditView.as_view(), name='present-edit'),
        path('delete/', views.PresentDeleteView.as_view(), name='present-delete'),
    ])),
]
