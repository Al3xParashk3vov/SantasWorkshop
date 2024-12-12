from django.contrib import admin
from django.core.exceptions import PermissionDenied

from SantasWorkshop.blogs.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    list_filter = ('created_date', 'author')
    search_fields = ('title', 'content')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.has_perm('blogs.can_view_all_posts'):
            return qs
        return qs.filter(author=request.user)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return (
                request.user.is_superuser or
                request.user == obj.author or
                request.user.has_perm('blogs.can_edit_others_posts')
        )

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return (
                request.user.is_superuser or
                request.user == obj.author or
                request.user.has_perm('blogs.can_delete_others_posts')
        )

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # New object
            obj.author = request.user
        elif not self.has_change_permission(request, obj):
            raise PermissionDenied
        super().save_model(request, obj, form, change)