from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from SantasWorkshop.blogs.forms import BlogPostForm, CommentForm
from SantasWorkshop.blogs.models import BlogPost, Comment


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        # Superusers and staff with view_all permission can see everything
        if self.request.user.is_superuser or self.request.user.has_perm('blogs.can_view_all_posts'):
            return BlogPost.objects.all()
        # Anonymous users only see published posts
        return BlogPost.objects.filter(status='published')


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object
        context['comments'] = Comment.objects.filter(post=self.object)
        return context


class BlogPostCreateView(PermissionRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/post_add.html'
    permission_required = 'can_publish_post'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogPostUpdateView(PermissionRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/post_edit.html'
    permission_required = 'can_edit_others_posts'

    def has_permission(self):
        obj = self.get_object()
        return super().has_permission() or obj.author == self.request.user


class BlogPostDeleteView(PermissionRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/post_delete.html'
    permission_required = 'can_delete_others_posts'

    def has_permission(self):
        obj = self.get_object()
        return super().has_permission() or obj.author == self.request.user


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.post = self.kwargs['pk']
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
