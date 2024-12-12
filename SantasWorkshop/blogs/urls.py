from django.urls import path, include

from SantasWorkshop.blogs import views

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('<int:pk>', include([
        path('', views.BlogPostDetailView.as_view(), name='post_detail'),
        path('edit/', views.post_edit, name='post_edit'),
        path('delete/', views.post_delete, name='post_delete'),
    ])),

]
