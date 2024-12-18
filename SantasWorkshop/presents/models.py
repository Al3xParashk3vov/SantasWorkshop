from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

# Create your models here.
class Present(models.Model):
    PRESENT_MAX_LENGTH = 40

    name = models.CharField(
        max_length=PRESENT_MAX_LENGTH,
        blank=False,
    )

    description = models.TextField(
        max_length=200,
        blank=False,
    )

    image = models.URLField(
        blank=False,
        help_text='Help Santa identify this present!',
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='presents'
    )