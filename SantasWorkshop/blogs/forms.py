from django import forms

from .mixins import DisableFieldsMixin
from .models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'preview_image',)

class BlogPostCreateForm(BlogPostForm):
    pass


class BlogPostEditForm(BlogPostForm):
    pass


class BlogPostDeleteForm(BlogPostForm, DisableFieldsMixin):
    disabled_fields = ('__all__',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')
