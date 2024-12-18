from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.utils.html import format_html

from SantasWorkshop.blogs.models import BlogPost, Comment


# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'created_date', 'published_date')
#     list_filter = ('created_date', 'author')
#     search_fields = ('title', 'content')
#
#     def comment_count(self, obj):
#         return obj.comments.count()
#
#     comment_count.short_description = 'Number of Comments'
#
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         elif request.user.has_perm('blogs.can_view_all_posts'):
#             return qs
#         return qs.filter(author=request.user)
#
#     def has_change_permission(self, request, obj=None):
#         if obj is None:
#             return True
#         return (
#                 request.user.is_superuser or
#                 request.user == obj.author or
#                 request.user.has_perm('blogs.can_edit_others_posts')
#         )
#
#     def has_delete_permission(self, request, obj=None):
#         if obj is None:
#             return True
#         return (
#                 request.user.is_superuser or
#                 request.user == obj.author or
#                 request.user.has_perm('blogs.can_delete_others_posts')
#         )
#
#     def save_model(self, request, obj, form, change):
#         if not obj.pk:  # New object
#             obj.author = request.user
#         elif not self.has_change_permission(request, obj):
#             raise PermissionDenied
#         super().save_model(request, obj, form, change)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_display', 'created_date', 'preview_image_display')
    list_filter = ('author', 'created_date')
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)

    fieldsets = (
        ('Post Content', {
            'fields': ('title', 'content', 'preview_image')
        }),
        ('Author & Date', {
            'fields': ('author', 'created_date'),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing existing object
            return ('created_date',)
        return ()

    def author_display(self, obj):
        return format_html(
            '<a href="/admin/auth/user/{}">{}</a>',
            obj.author.id,
            obj.author.username
        )

    author_display.short_description = 'Author'

    def preview_image_display(self, obj):
        if obj.preview_image:
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" style="max-width: 100px; max-height: 100px;" /></a>',
                obj.preview_image,
                obj.preview_image
            )
        return "No image"

    preview_image_display.short_description = 'Preview Image'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post_title', 'content_preview', 'created_at')
    list_filter = ('created_at', 'post')
    search_fields = ('author', 'content', 'post__title')
    raw_id_fields = ('post',)

    def post_title(self, obj):
        return obj.post.title

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    post_title.short_description = 'Blog Post'
    content_preview.short_description = 'Comment Preview'