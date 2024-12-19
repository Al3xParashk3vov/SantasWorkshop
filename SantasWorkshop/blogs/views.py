from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from SantasWorkshop.blogs.forms import BlogPostForm, CommentForm, CommentFormSet, CommentEditForm
from SantasWorkshop.blogs.models import BlogPost, Comment


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return BlogPost.objects.all().order_by('-created_date')


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post'] = self.object
    #     context['comments'] = Comment.objects.filter(post=self.object)
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = CommentFormSet(queryset=Comment.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        formset = CommentFormSet(request.POST, queryset=Comment.objects.none())

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()
            return redirect('post_detail', pk=post.pk)

        context = self.get_context_data()
        context['formset'] = formset
        return self.render_to_response(context)


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
    success_url = reverse_lazy('post_list')

    def has_permission(self):
        obj = self.get_object()
        return super().has_permission() or obj.author == self.request.user


class BlogPostDeleteView(PermissionRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/post_delete.html'
    permission_required = 'can_delete_others_posts'
    success_url = reverse_lazy('post_list')

    def has_permission(self):
        obj = self.get_object()
        return super().has_permission() or obj.author == self.request.user


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post = self.kwargs['pk']
        return super().form_valid(form)


class CommentEditView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentEditForm
    template_name = 'blog/comment_edit.html'

    def get_success_url(self):
        messages.success(self.request, 'Comment updated successfully.')
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = self.object
        return context


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Comment deleted successfully.')
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = self.object
        return context