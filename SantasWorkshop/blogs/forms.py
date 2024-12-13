from django import forms
from django.forms import modelformset_factory

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
        fields = ['author', 'content']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...',
                'rows': 3
            }),

        }
        error_messages = {
            'author': {
                'required': 'Write the name of the author',
            },
            'content': {
                'required': 'Write the content of the comment',
            },
        }

# Create the formset
CommentFormSet = modelformset_factory(
    Comment,
    form=CommentForm,
    extra=1,
)
