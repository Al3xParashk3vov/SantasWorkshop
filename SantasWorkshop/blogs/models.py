from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

UserModel = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    preview_image = models.URLField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_publish_post", "Can publish blog posts"),
            ("can_edit_others_posts", "Can edit posts by other users"),
            ("can_delete_others_posts", "Can delete posts by other users"),
            ("can_view_all_posts", "Can view all posts"),
        ]

    def publish(self):
        self.published_date = timezone.now()
        self.status = 'published'
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
