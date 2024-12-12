from django.urls import path, include

from SantasWorkshop.blogs import views

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='post_list'),
    path('post/new/', views.BlogPostCreateView.as_view(), name='post_new'),
    path('<int:pk>', include([
        path('', views.BlogPostDetailView.as_view(), name='post_detail'),
        path('edit/', views.BlogPostUpdateView.as_view(), name='post_edit'),
        path('delete/', views.BlogPostDeleteView.as_view(), name='post_delete'),
    ])),

]
