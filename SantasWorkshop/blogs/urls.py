from django.urls import path, include

from SantasWorkshop.blogs import views
from SantasWorkshop.blogs.views import CommentEditView, CommentDeleteView

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='post_list'),
    path('comment/<int:pk>/edit/', CommentEditView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('post/new/', views.BlogPostCreateView.as_view(), name='post_new'),
    path('<int:pk>', include([
        path('', views.BlogPostDetailView.as_view(), name='post_detail'),
        path('edit/', views.BlogPostUpdateView.as_view(), name='post_edit'),
        path('delete/', views.BlogPostDeleteView.as_view(), name='post_delete'),
    ])),

]